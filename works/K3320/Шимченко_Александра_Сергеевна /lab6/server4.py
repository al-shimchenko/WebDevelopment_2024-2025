import socket
import threading

clients = {}  

def handle_client(client_socket, client_address):
    try:
        name = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = name
        print(f"{name} подключился с адреса {client_address}.")
        broadcast(f"{name} вошёл в чат.", client_socket)

        while True:
            message = client_socket.recv(1024).decode('utf-8') 
            if message:
                print(f"{name}: {message}")
                broadcast(f"{name}: {message}", client_socket) 
    except:
        print(f"{clients[client_socket]} отключился.")
        broadcast(f"{clients[client_socket]} покинул чат.", client_socket)
        client_socket.close()
        del clients[client_socket]

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:  
            client.send(message.encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080)) 
    server_socket.listen(5) 

    print("Сервер запущен и ожидает подключения...")

    while True:
        client_socket, client_address = server_socket.accept()  
        print(f"Новое подключение: {client_address}")
        
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

start_server()