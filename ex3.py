from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome=nome
        self.matricula=matricula
        self.salario_base=salario_base
    
    @abstractmethod
    def calcula_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
    
    def calcula_salario(self):
        salGerente = self.salario_base * 2
        return salGerente

class Assistente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
    
    def calcula_salario(self):
        salAssistente = self.salario_base
        return salAssistente


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
    
    def calcula_salario(self):
        salVendedor= (self.salario_base * 0.1) + self.salario_base
        return salVendedor

TipoFuncionario = []

for f in range(1):
    nome = input('Digite seu nome:')
    matricula = input('Digite sua matricula:')
    salario_base = float(input('digite seu salario:'))
    gerente = Gerente(nome,matricula,salario_base)
    assistente = Assistente(nome,matricula,salario_base)
    vendedor = Vendedor(nome,matricula,salario_base)
    TipoFuncionario.append(gerente)
    TipoFuncionario.append(assistente)
    TipoFuncionario.append(vendedor)

for f in TipoFuncionario:
    print(f.nome, type(f).__name__,f.calcula_salario())#type pega o nome da class
  
#print(type(variavel ou objeto).__name__)