#Construindo métodos, funções e classes em Python
class Calculadora:

    def soma(self, valor_a, valor_b):
        return self.valor_a + self.valor_b

    def subtracao(self, valor_a, valor_b):
        return self.valor_a - self.valor_b

    def multiplicacao(self, valor_a, valor_b):
        return self.valor_a * self.valor_b

    def divisao(self, valor_a, valor_b):
        return self.valor_a / self.valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicacao(100, 2))
print(calculadora.divisao(10, 5))
