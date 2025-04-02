import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1) 

    print("Сервер ожидает подключения...")

    conn, addr = server_socket.accept()
    print(f"Подключение установлено: {addr}")

    client_message = conn.recv(1024).decode('utf-8')
    print(f"Сообщение от клиента: {client_message}")

    server_message = "Hello, client"
    conn.send(server_message.encode('utf-8'))
    
    conn.close()

start_server()