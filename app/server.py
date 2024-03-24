import socket
import threading    
from app.redis_request import RedisRequest
from app.database import Database
from argparse import ArgumentParser


class Server:
    def __init__(self):
        self.database = Database()
        
    def run(self):
        arg_parser = ArgumentParser()
        arg_parser.add_argument("--port", dest="port", default=6379, type=int)
        args = arg_parser.parse_args()
        server_socket = socket.create_server(("localhost", args.port), reuse_port=True)
        while True:
            connection, address = server_socket.accept()
            thread = threading.Thread(target=self.new_client, args=(connection, address))
            thread.start()

    def new_client(self, connection, address):
        while request := connection.recv(1024):
            redis_request = RedisRequest(request)
            redis_response = redis_request.response(self)
            connection.sendall(redis_response)
            
    
    