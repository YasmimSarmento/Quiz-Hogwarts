# coding: utf-8
import socket

# configuração do cliente
HOST = '127.0.0.1'
PORT = 5000

# cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("\nConectado ao servidor!\n")

# transforma o socket em arquivo
arquivo = client_socket.makefile('r', encoding='utf-8')

# todo o loop da comunicação
while True:
    mensagem = arquivo.readline().strip()

    if not mensagem:
        break

    partes = mensagem.split("|")
    comando = partes[0]

    if comando == "WELCOME":
        print("Olá, queridos!!\nBem vindo ao Quiz de Hogwarts")

    elif comando == "QUESTION":
        print(f"\nPergunta {partes[1]}:")
        print(partes[2])

    elif comando == "OPTION":
        print(f"{partes[1]}) {partes[2]}")

    elif comando == "ENDQUESTION":
        while True:
            resposta = input("Escolha uma opção (A/B/C/D): ").upper()
            if resposta in ["A", "B", "C", "D"]:
                break
            print("Opção inválida.")

        client_socket.sendall(
            f"ANSWER|{resposta}\n".encode("utf-8")
        )

    elif comando == "RESULT":
        print(f"\nSua casa é: {partes[1]}!!!! PARABÉNSSSS!!!!!\n")

    elif comando == "GOODBYE":
        print("Conexão encerrada pelo servidor, até breve :)\n")
        break

# fecha e encerra a conexão
arquivo.close()
client_socket.close()