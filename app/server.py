import socket
import threading    
from app.redis_request import RedisRequest
from app.database import Database
from app.redis_encoder import RedisEncoder
from random import random
import string

class Server:
    def __init__(self, port=6379, replica=[]):
        self.database = Database()
        
        # Default Server Settings
        self.master = True if not replica else False
        self.role = "master" if not replica else "slave"
        self.replica = replica
        
        # Random 40 char alphanum string
        self.master_replid = ''.join(random.choices(string.ascii_letter + string.digits, k=40))

        self.master_repl_offset =" 0"
        self.port = port
    
    def connect_to_master(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect(self.replica)
            sock.sendall(RedisEncoder.encode_arrays(["ping"]))
            data = sock.recv(1024)
            sock.close()
            return data

    def run(self):
        if self.replica:
            self.connect_to_master()
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
            

    