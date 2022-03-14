# para importar o mpodulo e biblioteca(programas e resursos do o.s)
import os

print("#" * 60)

# variavel que receberá um ip do usuário
ip_ou_host = input("Digite o Ip ou host a ser verificado: ")

print("-" * 60)

# chamando o system da bibioteca os | comando: -n num de pacotes que serão 6 no exemplo
os.system('1_ping -n 6 {}'.format(ip_ou_host))

print("-" * 60)
