import socket

portas = [21, 23, 80, 443, 8080]

for porta in portas:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    resposta = client.connect_ex(('bancocn.com', porta))

    if resposta == 0:
        print(porta, ' open')
        continue
    else:
        print(porta)
        continue
