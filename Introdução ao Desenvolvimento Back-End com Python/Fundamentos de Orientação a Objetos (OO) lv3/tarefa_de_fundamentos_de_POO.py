class Animal:  # Definição da classe base Animal
    def __init__(self, nome, idade):  # Método construtor (__init__) que inicializa um objeto Animal
        self.nome=nome  # Atribui o valor do parâmetro ao atributo 'nome' do objeto
        self.idade=idade  # Atribui o valor do parâmetro ao atributo 'idade' do objeto

    def emitir_som(self):  # Método para o animal emitir um som
        return "O animal emitiu um som genérico." # Retorna uma string genérica para o som do animal

class Cachorro(Animal): # Definição da classe Cachorro, que herda da classe Animal
   def emitir_som(self):  # Sobrescrita do método emitir_som para um comportamento específico de Cachorro
        return "O cachorro latiu!"  # Retorna o som característico do cachorro

class Gato(Animal):  # Definição da classe Gato, que herda da classe Animal
    def emitir_som(self):  # Sobrescrita do método emitir_som para um comportamento específico de Gato
        return "O gato miou!"  # Retorna o som característico do gato
    
cachorro=Cachorro("pit",10)
gato=Gato("trovão",4)

print(cachorro.emitir_som())
print(gato.emitir_som())
    