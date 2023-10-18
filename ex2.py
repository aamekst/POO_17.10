class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self):
        print ('AUUUUUU AUUUUU AUUUU')

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self):
        print ('MIAAAAAAAAAAAAAAAAAU')

class Cavalo(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self):
        print ('HIIIIIIIIIIHIHIHIHI')

class Veterinario:
    def examinar(self, animal):
        animal.emitir_som()

dog = Cachorro("Tyfani", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

print('-'*60)
vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato
