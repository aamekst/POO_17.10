from abc import ABC, abstractmethod

class Conta(ABC):               # classe abstrata
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
           
    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):     
        pass

    def imp_saldo(self):

        return self.saldo



class ContaCorrente(Conta):
    def __init__(self, numero, nome, saldo):
        super().__init__(numero, nome, saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print(f'Saque: {valor}')
            print("Saldo insuficiente")
        




class ContaPoupanca(Conta):
    def __init__(self, numero, nome, saldo):
        super().__init__(numero, nome, saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

        else:
            print(f'Saque: {valor}')
            print("Saldo insuficiente")





class ContaEspecial(Conta):
    def __init__(self, numero, nome, saldo, limite):
        super().__init__(numero, nome, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Limite insuficiente")

        return valor



cc = ContaCorrente(123, 'Paulo', 100)
cc.sacar(200)
cc.depositar(50)
print(f'Saldo Conta Corrente: {cc.imp_saldo()}')
print('-'*60)

cp = ContaPoupanca(124, 'João', 150)
cp.sacar(200)
cp.depositar(50)
print(f'Saldo Conta Poupança: {cp.imp_saldo()}')
print('-'*60)

ce = ContaEspecial(125, 'Tyfani', 200, 5000)
print(f'Saque: {ce.sacar(300)}')
ce.depositar(50)
print(f'Saldo Conta Especial: {ce.imp_saldo()}')
print('-'*60)