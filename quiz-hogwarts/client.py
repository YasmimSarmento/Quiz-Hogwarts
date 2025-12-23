import socket

# ------------------------------
# CONFIGURAÇÕES DO CLIENTE
# ------------------------------
HOST = '127.0.0.1'   # mesmo IP do servidor
PORT = 5000          # mesma porta do servidor

# ------------------------------
# CRIA SOCKET DO CLIENTE
# ------------------------------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((HOST, PORT))
print("Conectado ao servidor!\n")

# ------------------------------
# TRANSFORMA O SOCKET EM ARQUIVO
# (para ler linha por linha)
# ------------------------------
arquivo = client_socket.makefile('r')

# ------------------------------
# LOOP DE COMUNICAÇÃO
# ------------------------------
while True:
    mensagem = arquivo.readline().strip()

    if not mensagem:
        break

    partes = mensagem.split("|")
    comando = partes[0]

    # Boas-vindas
    if comando == "WELCOME":
        print("=== Bem-vindo ao Quiz de Hogwarts ===\n")

    # Pergunta
    elif comando == "QUESTION":
        print(f"\nPergunta {partes[1]}:")
        print(partes[2])

    # Opções
    elif comando == "OPTION":
        letra = partes[1]
        texto = partes[2]
        print(f"{letra}) {texto}")

    # Fim da pergunta → pedir resposta
    elif comando == "ENDQUESTION":
        while True:
            resposta = input("Escolha uma opção (A/B/C/D): ").upper()
            if resposta in ["A", "B", "C", "D"]:
                break
            print("Opção inválida. Digite apenas A, B, C ou D.")

        client_socket.sendall(f"ANSWER|{resposta}\n".encode())

    # Resultado final
    elif comando == "RESULT":
        casa = partes[1]
        print("\n===============================")
        print(f"Sua casa é: {casa}")
        print("===============================\n")

    # Encerramento
    elif comando == "GOODBYE":
        print("Conexão encerrada pelo servidor.")
        break

# ------------------------------
# FECHA CONEXÃO
# ------------------------------
arquivo.close()
client_socket.close()