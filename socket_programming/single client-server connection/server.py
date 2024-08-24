import socket

def start_server(host:str, port:int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server started at {host}:{port}")


        client_socket, client_addr = server_socket.accept()
        print(f"connection from {client_addr}")

        with client_socket:
            while True:
                data = client_socket.recv(1024).decode("utf-8")
                if not data:
                    break
                print(f"from client:{data}")
                client_socket.send(data.encode("utf-8"))
                    
        print("Connection closed, server turned off")




if __name__ == "__main__":
    host = "localhost"
    port = 65432

    start_server(host, port)
