import socket
import threading


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379))
    while connection := server_socket.accept():
        conn, addr = connection
        thread = threading.Thread(target=respond, args=[conn])
        thread.start()
    
    def respond(conn):
        res = "+PONG\r\n"
        with conn:
            while req := conn.recv(1024):
                conn.sendall(res.encode())
            

if __name__ == "__main__":
    main()
