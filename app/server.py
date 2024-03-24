import socket
import threading    
from app.redis_request import RedisRequest
from app.database import Database

class Server:
    def __init__(self, port=6379):
        self.database = Database()
        self.role = "master"
        self.port = port
    def run(self):
        server_socket = socket.create_server(("localhost", self.port), reuse_port=True)
        
        while True:
            connection, address = server_socket.accept()
            thread = threading.Thread(target=self.new_client, args=(connection, address))
            thread.start()

    def new_client(self, connection, address):
        while request := connection.recv(1024):
            redis_request = RedisRequest(request)
            redis_response = redis_request.response(self)
            connection.sendall(redis_response)
            
    
    