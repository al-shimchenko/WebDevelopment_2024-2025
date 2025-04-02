import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    client_message = "Hello, server"
    client_socket.send(client_message.encode('utf-8'))

    server_message = client_socket.recv(1024).decode('utf-8')
    print(f"Сообщение от сервера: {server_message}")
    
    client_socket.close()

start_client()