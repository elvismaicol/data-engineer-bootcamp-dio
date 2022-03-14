import random, string

# Em boas práticas em Seg. Inform. tamanho 16
tamanho = int(input('Digite o tamanho de senha que você deseja: '))

# ascii_letters => letras Maiusculas e Minusculas
# ascii_lowercase => letras Minusculas
#ascii_uppercase => letras Maiusculas
chars = string.ascii_letters + string.digits + '!@#%&*()-='

# SystemRandom() => usa os.urandom, que gera nº aleatórios a partir de fontes do S.O.
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))