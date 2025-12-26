# coding: utf-8
import socket

# CONFIGURAÇÕES DO SERVIDOR
HOST = '127.0.0.1'   # localhost
PORT = 5000          # porta do servidor

# PERGUNTAS DO QUIZ
perguntas = [
    {
        "texto": "Diante de um desafio, você costuma:",
        "opcoes": {
            "A": "Enfrentar sem hesitar",
            "B": "Analisar antes de agir",
            "C": "Pensar em como ajudar os outros",
            "D": "Agir de forma estratégica"
        }
    },
    {
        "texto": "Qual dessas qualidades você mais valoriza?",
        "opcoes": {
            "A": "Coragem",
            "B": "Inteligência",
            "C": "Lealdade",
            "D": "Ambição"
        }
    },
    {
        "texto": "No seu grupo de amigos, você geralmente é quem:",
        "opcoes": {
            "A": "Toma a frente das situações",
            "B": "Dá boas ideias",
            "C": "Mantém o grupo unido",
            "D": "Define objetivos"
        }
    },
    {
        "texto": "Em Hogwarts, você preferiria passar o tempo livre:",
        "opcoes": {
            "A": "Explorando lugares proibidos",
            "B": "Estudando na biblioteca",
            "C": "Conversando com amigos",
            "D": "Planejando seu futuro"
        }
    },
    {
        "texto": "Quando algo dá errado, você tende a:",
        "opcoes": {
            "A": "Agir rapidamente",
            "B": "Pensar em uma solução lógica",
            "C": "Apoiar quem está ao seu redor",
            "D": "Transformar o erro em vantagem"
        }
    },
    {
        "texto": "O que mais te motiva?",
        "opcoes": {
            "A": "Fazer o que é certo",
            "B": "Aprender sempre mais",
            "C": "Pertencer a um grupo",
            "D": "Alcançar o sucesso"
        }
    }
]

# MAPEAMENTO DAS RESPOSTAS
mapa_casas = {
    "A": "Grifinória",
    "B": "Corvinal",
    "C": "Lufa-Lufa",
    "D": "Sonserina"
}

# CRIAÇÃO DO SOCKET
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Servidor aguardando conexão...")

client_socket, client_address = server_socket.accept()
print(f"Cliente conectado: {client_address}")

# INÍCIO DA COMUNICAÇÃO CLIENTE/SERVIDOR
client_socket.sendall("WELCOME\n".encode("utf-8"))

pontuacao = {
    "Grifinória": 0,
    "Corvinal": 0,
    "Lufa-Lufa": 0,
    "Sonserina": 0
}

resposta_desempate = None

for indice, pergunta in enumerate(perguntas):
    # Envia pergunta
    mensagem = f"QUESTION|{indice + 1}|{pergunta['texto']}\n"
    client_socket.sendall(mensagem.encode("utf-8"))

    # Envia opções
    for letra, texto in pergunta["opcoes"].items():
        opcao = f"OPTION|{letra}|{texto}\n"
        client_socket.sendall(opcao.encode("utf-8"))

    client_socket.sendall("ENDQUESTION\n".encode("utf-8"))

    # Recebe resposta
    resposta = client_socket.recv(1024).decode("utf-8").strip()
    _, alternativa = resposta.split("|")

    casa = mapa_casas.get(alternativa)
    pontuacao[casa] += 1

    if indice == len(perguntas) - 1:
        resposta_desempate = casa

# CÁLCULO DO RESULTADO
maior_pontuacao = max(pontuacao.values())
casas_empate = [casa for casa, pontos in pontuacao.items() if pontos == maior_pontuacao]

if len(casas_empate) == 1:
    casa_final = casas_empate[0]
else:
    casa_final = resposta_desempate

# ENVIA O RESULTADO
resultado = f"RESULT|{casa_final}\n"
client_socket.sendall(resultado.encode("utf-8"))

client_socket.sendall("GOODBYE\n".encode("utf-8"))

client_socket.close()
server_socket.close()

print("Servidor encerrado.")