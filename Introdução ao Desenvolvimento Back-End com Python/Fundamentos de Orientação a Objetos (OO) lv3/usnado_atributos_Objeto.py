#Molde do Pokemon

#Vamos ter Vários atributos

#A classe é o molde que vamos criar para poder conseguirmos contruir coisas

class MoldePokemon:
    #Metodo contrutor
    #Self tem a responsabilidade de armazenar a manipilar essas informações dos atributos
    def __init__(self,nome,altura,peso,hp,ataque,tipo):
        self.nome=nome
        self.altura=altura
        self.peso=peso
        self.hp=hp
        self.ataque=ataque
        self.tipo=tipo
    
    def mostrar_nome_pokemon(self):
        print(f"o nome do meu Pokemon é: {self.nome}")
    
    def mostrar_altura_pokemon(self):
        print(f"A altura do meu pokemon é: {self.altura}")

    def mostrar_peso_pokemon(self):
        print(f"o peso do meu pokemon é: {self.peso}")
    
    def mostrar_ataque_pokemon(self):
        print(f"o ataque desse pokemon é: {self.ataque}")
    def mostrar_tipo_pokemon(self):
        print(f"o tipo de pokemon é: {self.tipo}")

#chegou a hora de pegar essa classe(class:MoldePokemon) e de fato contruir essas coisas
#por enquanto, a gente ainda tem apenas o molde
#contruir dentro da Orientação a Objetos significa criar um Objeto

buba=MoldePokemon("BUBASAURO",0.50,20,1057,"maconha infinatira","NATUREZA")
pika=MoldePokemon("pika no cu", 0.17,0.300, 4,"porra flamejante","SEXO")


buba.mostrar_nome_pokemon()
buba.mostrar_peso_pokemon()
buba.mostrar_altura_pokemon()

pika.mostrar_nome_pokemon()
pika.mostrar_altura_pokemon()
pika.mostrar_peso_pokemon()
pika.mostrar_ataque_pokemon()
pika.mostrar_tipo_pokemon()
    