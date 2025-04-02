import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080)) 

    try:
        a = input("Введите значение первого катета: ")
        b = input("Введите значение второго катета: ")

        if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
            raise ValueError("Введены нечисловые значения")
        
        a, b = float(a), float(b)
        if a <= 0 or b <= 0:
            raise ValueError("Значения должны быть положительными")

        client_socket.send(f"{a},{b}".encode('utf-8'))

        result = client_socket.recv(1024).decode('utf-8')
        print(result)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        client_socket.close()

start_client()