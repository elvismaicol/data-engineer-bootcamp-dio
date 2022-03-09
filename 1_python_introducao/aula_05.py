lista = [1, 3, 5, 7]
lista2 = [12, 10, 7, 5]

#Ordenar lista
print(lista2)
lista2.sort()
print('Lista ordenada:')
print(lista2)
# invertendo a lista
print('Lista invertida:')
lista2.reverse()
print(lista2)


# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print('Soma 1: ' + str(soma))
# print('Soma 2: ' + str(sum(lista)))

##########
print()
lista_animal = ['cachorro', 'gato', 'elefante']
lista_animal2 = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

# Ordenar lista
print(lista_animal2)
print('Lista ordenada:')
lista_animal2.sort()
print(lista_animal2)
# invertendo a lista
print('Lista invertida:')
lista_animal2.reverse()
print(lista_animal2)

# Inserindo item na lista
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista')
#     lista_animal.append('lobo')
#     print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)

# lista_animal.pop(1)
# print(lista_animal)

# nova_lista = lista_animal * 3
# print(nova_lista)

# print(lista_animal[1])

# for x in lista_animal:
#     print(x)
#
# print(max(lista_animal))

# TUPLA
print()
print('TUPLAS')
tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal2))
tupla_animal = tuple(lista_animal2)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)
