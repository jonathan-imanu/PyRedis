import socket
import threading    
from app.redis_request import RedisRequest



class Server:
    def __init__(self):
        self.db = {}
        
    def run(self):
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        while True:
            connection = server_socket.accept()
            thread = threading.Thread(
                target=self.client_thread, args=(connection)
            )
            thread.start()

    def client_thread(self, connection):
        # conn, addr = connection
        # while True:
        #     request = conn.recv(1024)
        #     if not request:
        #         connection.close()
        #         break
        #     redis_request = RedisRequest(request)
        #     redis_response = redis_request.response(self)
        #     connection.sendall(redis_response)
        # connection.close()
        conn, addr = connection
        while request := conn.recv(1024):
            redis_request = RedisRequest(request)
            redis_response = redis_request.response(self)
            conn.sendall(redis_response)
            
    
    