#Construindo métodos, funções e classes em Python
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())



# print(soma(1, 2))
# print(soma(3, 5))
# print(subtracao(10, 12))
# print(multiplicacao(10, 12))
# print(divisao(10, 12))
