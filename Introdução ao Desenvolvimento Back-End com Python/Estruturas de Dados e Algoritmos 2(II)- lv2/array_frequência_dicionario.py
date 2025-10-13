#dado um array de inteiros meu_arrayzinho, um inteiro sortudo é um inteiro que tem uma frequencia no array igual ao seu valor. 

meu_arrayzinho=[1,2,2,3,3,3,4,4,5,6,7,7,8,8,8,8,8,8,8,8]

#1.Criar um dicionário para adicionar todos os valores, descobrindo, assim, as chaves e valores
#A Chave sendo o numero e o valor sendo a frequência(ou seja, a quantidade de vezes que esse número apareceu no array) 

meu_dicionariozinho={}

for i in meu_arrayzinho:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i]=1
    else:
        meu_dicionariozinho[i]+=1
    
for chave,valor in meu_dicionariozinho.items():
    if chave==valor:
        print(chave)