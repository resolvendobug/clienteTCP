import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    except socket.error as ex:
        print("Conexão falhou!")
        print("Erro: {}".format(ex))
        sys.exit()
    
    print("Socket criado com sucesso!")

    Host = input("Digite o Host ou IP:")
    port = input("Digite a Porta:")

    try:
        s.connect((Host , int(port)))
        print("Conectado com sucesso!")
        s.shutdown(2)
    except socket.error as ex:
        print("Conexão falhou!")
        print("Erro: {}".format(ex))
        sys.exit()

if __name__ == "__main__":
    main()