import socket
import sqlite3
import threading


# Создаем базу данных и таблицу для пользователей
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()


# Добавление пользователя в базу данных
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


# Проверка пользователя в базе данных
def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


# Обработка клиентских соединений
def handle_client(client_socket):
    auth_data = client_socket.recv(1024).decode()
    username, password = auth_data.split(',')

    if authenticate(username, password):
        client_socket.send("AUTH_SUCCESS".encode())
    else:
        client_socket.send("AUTH_FAILURE".encode())

    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Сервер запущен и слушает соединения...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    init_db()
    add_user("user1", "password1")
    add_user("user2", "password2")
    start_server()
