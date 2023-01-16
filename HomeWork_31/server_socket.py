import socket
import requests

def server():
    host = socket.gethostname()
    port = 5002

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    print('Waiting connection...')
    conn, address = server_socket.accept()
    print(f'Connection from : {str(address)}')

    while True:
        data = conn.recv(1024).decode()
        print(f"From connected user {str(address)}: {str(data)}")
        try:
            response = requests.get(str(data))

            response.raise_for_status()
        except Exception as err:
            conn.send(str(err).encode())
        else:
            conn.send(response.content)

server()




