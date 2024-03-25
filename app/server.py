import socket
import threading    
from app.redis_request import RedisRequest
from app.database import Database
from random import random
import string

class Server:
    def __init__(self, port=6379, replica=[]):
        self.database = Database()
        
        # Default Server Settings
        self.master = True
        self.role = "master"
        self.replica = []
        
        self.master_replid= (''.join(random.choices(string.ascii_lowercase, k=40))) # Needs to changed to a random 40 char alphanum string
        self.master_repl_offset="0"
        
        if replica:
            self.role = "slave"
            self.replica = replica
        
       
         
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
            
    def isReplica(self):
        pass
    