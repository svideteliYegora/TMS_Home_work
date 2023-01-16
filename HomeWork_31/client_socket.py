import socket


def client():
    host = socket.gethostname()
    port = 5002

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input('--> ')

    while message != 'close':
        client_socket.send(message.encode())

        data = client_socket.recv(1024).decode()
        print(f"Recieved from server: {data}")

        message = input('--> ')

    client_socket.close()

client()

