# Quiz de Hogwarts – Cliente/Servidor em Python

Este projeto consiste em uma **aplicação cliente/servidor desenvolvida em Python** para a disciplina **Redes de Computadores I (2025.4)**.
A aplicação implementa um **quiz no terminal** cujo objetivo é identificar a **casa de Hogwarts** do usuário, utilizando comunicação em rede baseada em **sockets TCP** e um **protocolo de aplicação próprio**.

## Autores
- Bruno da Silva Lopes  
- Emmanoel Victor Barros da Cruz  
- Yasmim Cristina Sarmento da Poça
  
**Disciplina:** Redes de Computadores I – 2025.4

---

## Objetivo

O objetivo do projeto é aplicar, de forma prática, os conceitos estudados na disciplina de **Redes de Computadores**, incluindo:

- Arquitetura cliente/servidor  
- Comunicação via sockets TCP  
- Desenvolvimento de protocolo de aplicação  
- Controle e encerramento de conexões  
- Troca de mensagens entre processos distribuídos  

Todo o sistema foi desenvolvido **sem o uso de frameworks ou bibliotecas externas**, utilizando apenas a biblioteca padrão `socket` do Python.

---

## Descrição da Aplicação

A aplicação é composta por dois programas distintos:

### Servidor (`server.py`)

Responsável por:

- Aguardar conexões de clientes  
- Enviar perguntas e alternativas  
- Receber respostas do cliente  
- Calcular o resultado final do quiz  
- Encerrar a conexão de forma controlada  

### Cliente (`client.py`)

Responsável por:

- Conectar-se ao servidor  
- Exibir as perguntas no terminal  
- Capturar e enviar as respostas do usuário  
- Receber e exibir o resultado final  

A comunicação ocorre por meio de **mensagens textuais delimitadas por linha**, seguindo um protocolo definido pelos próprios autores.

---

## Protocolo de Aplicação

O protocolo de comunicação é baseado em comandos textuais separados pelo caractere `|`.

Exemplos de mensagens utilizadas:

- `WELCOME`  
- `QUESTION|id|texto`  
- `OPTION|letra|texto`  
- `ENDQUESTION`  
- `RESULT|casa`  
- `GOODBYE`  

Esse protocolo evidencia que a **semântica das mensagens é definida pela aplicação**, e não pelo protocolo de transporte.

---

## Decisões de Projeto

Inicialmente, o projeto foi idealizado como um quiz para identificar **qual personagem do universo Harry Potter** representaria o usuário.  
Entretanto, essa abordagem apresentou **maior complexidade lógica**, principalmente na diferenciação entre personagens e no tratamento de empates. Dessa forma, optou-se por **simplificar o escopo da aplicação**, mantendo o tema, mas focando apenas na **identificação das casas de Hogwarts**, o que permitiu:
- Regras mais claras  
- Menor complexidade  
- Melhor aderência aos objetivos da disciplina  

---

## Tecnologias Utilizadas

- Python 3  
- Biblioteca padrão `socket`  
- Protocolo TCP  
- Execução em terminal  

---

## Como Executar

1. Inicie o servidor no terminal do VS Code:
   ```bash
   python server.py
2. Em outro terminal, execute o cliente:
   ```bash
   python client.py
