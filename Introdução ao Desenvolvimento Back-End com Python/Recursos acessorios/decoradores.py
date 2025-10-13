def meu_decorator(func):
    def wrapper():
        print("Antes da execução da minha função!")
        func()
        print("depois da execução da minha função!")
    return wrapper

@meu_decorator
def despedida():
    print("Tchau!")
    
@meu_decorator
def chegada():
    print("chegeui")
    

chegada()
despedida()