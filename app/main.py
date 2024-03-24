from app.server import Server

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server = Server()
    server.run()
        
if __name__ == "__main__":
    main()
