import socket
import threading

def respond(conn):
    response = "+PONG\r\n"
    with conn:
        while req := conn.recv(1024):
            conn.send(response.encode())

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while connection := server_socket.accept():
        conn, addr = connection
        thread = threading.Thread(target=respond, args=[connection])
        thread.start()
        
if __name__ == "__main__":
    main()
