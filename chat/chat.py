import socket
import threading
import sys
import time

# SERVER
MY_HOST = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
PORT = 5000
MY_ADDRESS = (MY_HOST, PORT)

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(MY_ADDRESS)

# CLIENT
if len(sys.argv) < 2:
    print("Please provide the server's IP address")
    sys.exit(1)
distant_server_ip = sys.argv[1]


def start_server():
    server_socket.listen()
    connection, address = server_socket.accept()
    print("Connected to:", address)
    while True:
        message = connection.recv(1024).decode()
        if message.lower().strip() == "bye":
            break
        print(f"{address} _> {message}")
        connection.send("ok".encode())
    print("Closing server connection...")
    connection.close()
    server_socket.close()


def start_client():
    connected = False
    while not connected:
        try:
            print("Connecting to server %s:%d..." % (distant_server_ip, PORT))
            client_socket = socket.socket()
            client_socket.connect((distant_server_ip, PORT))
            connected = True
        except ConnectionRefusedError:
            print("Connection refused. Retrying in 10 seconds...")
            time.sleep(10)
            continue

    while True:
        message = input(" -> ")
        client_socket.send(message.encode())
        if message.lower().strip() == "bye":
            break
        response = client_socket.recv(1024).decode()
        print("Server response:", response)
    print("Closing client connection...")
    client_socket.close()


if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    start_client()
