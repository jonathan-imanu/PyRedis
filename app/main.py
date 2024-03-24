from argparse import ArgumentParser
from app.server import Server

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    arg_parser = ArgumentParser()
    arg_parser.add_argument("--port", dest="port", default=6379, type=int, help="The port on which to run the server")
    args = arg_parser.parse_args()
    
    server = Server(args.port)
    server.run()
        
if __name__ == "__main__":
    main()
