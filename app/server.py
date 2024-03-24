import socket
import threading    
from app.redis_request import RedisRequest

class Server:
    def __init__(self, directory=None):
        self.directory = directory
    def run(self):
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        while connection := server_socket.accept():
            conn, addr = connection
            thread = threading.Thread(self.new_client, args=connection)
            thread.start()
            
    def new_client(self, connection):
        conn, addr = connection
        while req := conn.recv(1024):
            redis_request = RedisRequest(req)
            redis_response = redis_request.response()
            connection.sendall(redis_response)
        connection.close()