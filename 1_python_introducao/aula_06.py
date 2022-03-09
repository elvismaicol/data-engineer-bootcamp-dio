#Conjuntos

conjunto = {1, 2, 3, 4}
print(conjunto)

print('Adicionando')
conjunto.add(5)
print(conjunto)
print('Removendo')
conjunto.discard(2)
print(conjunto)

#Unindo conjuntos
print()
print('Unindo conjuntos')
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

#Intersecção conjuntos
print()
print('Intersecção conjuntos')
conjunto_interseccao = conjunto1.intersection(conjunto2)
print(conjunto_interseccao)

#Diferença conjuntos
print()
print('Diferença conjuntos')
conjunto_diferença_1 = conjunto1.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferença_1))
conjunto_diferença_2 = conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferença_2))

#Diferença Simetrica
print()
print('Diferença Simetrica')
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença Simetrica: {}'.format(conjunto_diff_simetrica))

#Subset
print()
print('Conjunto Subset')
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B: {}'.format(conjunto_subset))
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('B é um subconjunto de A: {}'.format(conjunto_subset2))

#SuperSet
print()
print('SuperSet')
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é um superconjunto de B: {}'.format(conjunto_superset))
conjunto_superset2 = conjunto_b.issuperset(conjunto_a)
print(('B é um superconjunto de A: {}'.format(conjunto_superset2)))

# Retirando Duplicidade de uma lista
print()
lista_animais = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista_animais)
#convertendo para conjunto
conjunto_animais = set(lista_animais)
print(conjunto_animais)
#convertendo para lista
lista_animais_unicos = list(conjunto_animais)
print(lista_animais_unicos)
