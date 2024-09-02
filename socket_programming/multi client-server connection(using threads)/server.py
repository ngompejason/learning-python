import socket
import threading

def start_server(host="localhost", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server Hosted at:{host}:{port}")

        while True:
            client_socket, client_addr = server_socket.accept()
            print(f"Connection from {client_addr}")
            c_thread = threading.Thread(target=handle_clients, args = (client_socket,))
            c_thread.start()


def handle_clients(socket):
    with socket:
        while True:
            data = socket.recv(1024).decode("utf-8")
            if not data:
                break
            print(f"From client: {data}")
            data = socket.send(b"keep going")

if __name__ == "__main__":
    
    start_server()