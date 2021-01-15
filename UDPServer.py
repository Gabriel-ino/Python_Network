import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('\033[1;34mSocket criado com sucesso!')
host = 'localhost'
port = 5432

sock.bind((host, port))

while 1:
    data, end = sock.recvfrom(4096)
    print(data.decode())
    if data:
        print('Enviando mensagem...')
        sock.sendto('Hello from the world'.encode(), end)
