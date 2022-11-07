import socket
import datetime
import json

time = datetime.datetime.now().time()
hour = time.hour
min = time.minute


def run():
    server_socket = socket.socket()
    server_socket.bind(("localhost", 6666))
    server_socket.listen(10)  # Делает сервером(слушает порты)

    while True:
        conn, addr = server_socket.accept()  # подключениек клиента
        request = conn.recv(1024)  # размер передоваемого файла
        conn.sendall(
            "{}\n{}:{} Добрый день, направляю ваш запрос в СП".format(request.decode("utf-8"), time.hour,
                                                                      time.minute).encode(
                "utf-8"))  # ответ пользователю
        conn.close()


if __name__ == '__main__':
    run()
