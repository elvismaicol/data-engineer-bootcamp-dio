a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(f'soma: {soma}. '
      f'\nSubtração: {subtracao}. '
      f'\nMultiplicacao: {multiplicacao}. '
      f'\nDivisao: {divisao}. '
      f'\nResto: {resto}'
      .format(soma=soma
              , subtracao=subtracao
              , multiplicacao=multiplicacao
              , divisao=divisao
              , resto=resto))
# print('soma: ' + str(soma))
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(resto)
