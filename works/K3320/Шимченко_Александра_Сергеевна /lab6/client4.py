import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8') 
            print(message)
        except:
            print("Отключение от сервера.")
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080)) 

    name = input("Введите ваше имя: ")
    client_socket.send(name.encode('utf-8')) 

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        try:
            message = input() 
            client_socket.send(message.encode('utf-8'))  
        except:
            client_socket.close()
            break

start_client()