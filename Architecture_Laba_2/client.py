import socket


def authenticate(username, password):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    auth_data = f"{username},{password}"
    client.send(auth_data.encode())

    response = client.recv(1024).decode()
    client.close()

    if response == "AUTH_SUCCESS":
        print("Успешная авторизация!")
    else:
        print("Ошибка авторизации. Неверный логин или пароль.")


if __name__ == "__main__":
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    authenticate(username, password)
