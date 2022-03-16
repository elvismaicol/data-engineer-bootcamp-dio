import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso.")

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = "\nServidor: Olá cLiente tudo certo?"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviado mensagem...')
        s.sendto(dados + (mensagem.encode()), end)
