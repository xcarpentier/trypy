import socket

MY_HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
MY_ADDRESS = (MY_HOST, PORT)

socket = socket.socket()
socket.bind(MY_ADDRESS)
socket.listen()


def start():
    while True:
        connection, address = socket.accept()
        message = connection.recv(1024).decode()
        print(f"{address} _> {message}")
