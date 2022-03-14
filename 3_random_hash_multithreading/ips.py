import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

# Exemplo de operação com ip
print(endereco + 256)
print(endereco + 2000)

print('-' * 60)

# Trabalhando com redes
ip2 = "192.168.0.0/4"

# strict=False => verifica se é ip de rede válido (=False desliga a validação)
rede = ipaddress.ip_network(ip2, strict=False)

for ip2 in rede:
    print(ip2)
