import socket
from time import sleep as slp

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('\033[1;34mCliente criado com sucesso')
host = 'localhost'
port = 5433
try:
    sock.sendto('Hello World'.encode(), (host, 5432))
    data, server = sock.recvfrom(4096)
    data = data.decode()
    print(data)

finally:
    print('Fechando a conexão', end='')
    for c in range(0, 3):
        print('.', end='')
        slp(0.7)
    sock.close()
