import socket
import sys


def main():
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as E:
        print(f'\033[1;31mA conexão falhou.\nErro: {E}')
        sys.exit()
    print('\033[1;34mA conexão foi criada com sucesso!')

    host = str(input('Digite o host ou IP a ser conectado:')).strip()
    port = str(input('Digite a porta a ser conectada:')).strip()

    try:
        conn.connect((host, int(port)))
        print(f'\033[1;34mCliente TCP conectado com sucesso!\nHost: {host} \n Porta: {port}')
        conn.shutdown(2)

    except socket.error as E:
        print(f'\033[1;31mA conexão falhou.\nErro: {E}')
        sys.exit()

main()

