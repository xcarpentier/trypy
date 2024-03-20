import socket

host = socket.gethostbyname(socket.gethostname())
print(host)
port = 5000

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen()
conn, address = server_socket.accept()  # wait for connection
print("Waiting for connection...")
print("Connection from: " + str(address))
while True:
    data = conn.recv(1024).decode()
    if data == "bye":
        break
    print("from connected user: " + str(data))
    conn.send(data.encode())

conn.close()  # close the connection
