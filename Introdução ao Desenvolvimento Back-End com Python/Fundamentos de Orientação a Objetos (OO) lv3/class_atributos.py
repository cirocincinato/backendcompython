#uma classe é um Molde.
#vamos usar esse Molde para contruir 
# coisas que queremos que tenham um mesmo padão.

# - nome
# - Hp
# - Tipo do meu Pokemon(Terra, Eletrico, Fogo, etc)
# - Quais seus ataques(Choque do trovão)
# - Altura
# - Pesso 

# nome -> Pikachu
# HP -> 300
# Tipo -> Eletrico
# Ataque -> choque do Trovão
# Altura -> 50 cm
# Pesso -> 15 kg

# Nome -> Charizard
# HP -> 400
# tipo -> fogo
# Ataque -> Lança chamas 
# Altura -> 2m
# Peso -> 130 kg

class MoldePokemon:
    #Metodo contrutor
    #Self tem a responsabilidade de armazenar a manipilar essas 
    def __init__(self,nome,hp,tipo,ataque,altura,peso):
        self.nome=nome
        self.hp=hp
        self.tipo=tipo
        self.ataque=ataque
        self.altura=altura
        self.peso=peso

    def mostrar_nome_pokemon(self):
        print(f"nome do pokemon é {self.nome}")
    