def soma_de_numeros(x,y):
    return x+y

print("ssaaaaaaaaaaaa",soma_de_numeros(4,5))

soma=lambda x,y:x+y  

print(soma(5,4))

meu_arrayzinho=["1 - ","2 - ","3 - ","4 - "]

duplicados=map(lambda numero: numero+numero,meu_arrayzinho)
print(list(duplicados))