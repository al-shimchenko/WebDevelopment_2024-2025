import socket
import math

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080)) 
    server_socket.listen(1) 

    print("Сервер ожидает подключения...")

    conn, addr = server_socket.accept()
    print(f"Подключение установлено: {addr}")

    try:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            raise ValueError("Получено пустое сообщение")
        
        a, b = map(float, data.split(',')) 
        print(f"Получены параметры: a={a}, b={b}")
        
        if a <= 0 or b <= 0:
            raise ValueError("Значения должны быть положительными")

        c = math.sqrt(a**2 + b**2)
        print(f"Вычисленный результат: c={c}")
        
        conn.send(f"Гипотенуза: {c}".encode('utf-8'))
    except ValueError as e:
        error_message = f"Ошибка: {e}"
        print(error_message)
        conn.send(error_message.encode('utf-8'))
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        conn.send("Ошибка: Некорректные данные".encode('utf-8'))
    finally:
        conn.close()

start_server()