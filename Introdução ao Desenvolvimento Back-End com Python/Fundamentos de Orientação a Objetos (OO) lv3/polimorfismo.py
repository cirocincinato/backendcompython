#Polimorfismo

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "au au!"

class Gato(Animal):
    def falar(self):
        return "miau miau!"
    
animais = [Cachorro(),Gato()]

for animal in animais:
    print(animal.falar())
    

