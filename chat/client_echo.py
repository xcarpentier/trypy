import socket

host = "???"
port = 5000

client_socket = socket.socket()
client_socket.connect((host, port))  # server doit être démarré avant le client

message = input(" -> ")

while message.lower().strip() != "bye":
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    print("Received from server: " + data)

    message = input(" -> ")

client_socket.close()
