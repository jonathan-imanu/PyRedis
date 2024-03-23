import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.accept() 
    conn, server = server_socket.accept()
    with conn:
        req = conn.recv(1024)
        resp = b"+PONG\r\n"
        conn.sendall(resp)

if __name__ == "__main__":
    main()
