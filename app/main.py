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
        data = conn.recv(1024)
        res = "+PONG\r\n"
        conn.sendall(res.encode())

if __name__ == "__main__":
    main()
