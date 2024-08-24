import socket

def start_client(host:str, port:int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        while True:
            message = input("-> ")
            if message.lower().strip() == "closed":
                break
            client_socket.send(message.encode("utf-8"))
            data = client_socket.recv(1024).decode("utf-8")
            print(f"Server: {data}")
        
        print("Connection closed, server turned off")



if __name__ == "__main__":
    host = "localhost"
    port = 65432

    start_client(host, port)
