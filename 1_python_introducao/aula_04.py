a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    c = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))

#While
# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota: '))

#For
# a = int(input('Entre com o número: '))
#
# for num in range(a + 1):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         #rint(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('Número {} é primo.'.format(a))
# else:
#     print('Número {} não é primo.'.format(a))


# for x in range(101):
#     print(x)