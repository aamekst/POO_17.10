#italic - abstrato
from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def calcular(self, x, y):
        pass

 
class Soma(Operacao): #TEM QUE TER RETURN
    def calcular(self, x, y):
        return  x+y
        
class Subtracao(Operacao):
    def calcular(self, x, y):
        return  x-y
    
class Multiplicacao(Operacao):
    def calcular(self, x, y):
        return  x*y
    
class Divisao(Operacao):
    def calcular(self, x, y):
        div = x/y
        return  div

soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

som1 = int(input('valor: '))
som2 = int(input('valor 2: '))

print(f'Soma: {soma.calcular(som1, som2)}')
print(f'Subtração: {sub.calcular(10, 5)}')
print(f'Divisão: {div.calcular(10, 5)}') 
print(f'Multiplicação: {mult.calcular(10, 5)}') 