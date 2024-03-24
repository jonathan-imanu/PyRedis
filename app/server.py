import socket
import threading    
from app.redis_request import RedisRequest

# class Server:
#     def __init__(self, directory=None):
#         self.directory = directory
#     def run(self):
#         server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
#         while connection := server_socket.accept():
#             conn, addr = connection
#             thread = threading.Thread(self.new_client, args=connection)
#             thread.start()
            
#     def new_client(self, connection):
#         conn, addr = connection
#         while req := conn.recv(1024):
#             redis_request = RedisRequest(req)
#             redis_response = redis_request.response()
#             connection.sendall(redis_response)
#         connection.close()

class Server:
    """
    Server class that handles communication
    """
    def __init__(self, directory=None):
        self.directory = directory
    def run(self):
        """
        Runs the server to handle parallel connections
        :return:
        """
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        while True:
            connection, address = server_socket.accept()
            thread = threading.Thread(
                target=self.client_thread, args=(connection, address)
            )
            thread.start()
    def client_thread(self, connection, address):
        """
        Method that handles communication between server and a single connection
        :param connection:
        :param address:
        :return:
        """
        while True:
            request = connection.recv(1024)
            if not request:
                connection.close()
                break
            redis_request = RedisRequest(request)
            redis_response = redis_request.response()
            connection.sendall(redis_response)
        connection.close()