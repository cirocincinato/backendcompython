#Você recebe um array de numeros inteiros meu_arrayzinho.
#Os elementos únicos de um arry são os elementos que aparecem exatamente uma vez no array
#retone a soma de todos os elementos unicos de meu_arrayzinho

meu_arrayzinho=[1,2,5,41,4,1,2,1,5,4,6,2,1,5]
#41+6 = 47
"""
1-4
2-3
4-2
5-3
6-1
41-1
CHAVE - VALOR (é exatamente um dicionario kkk)
"""

#criar um dicionario (uma estrutura de dados) para adicionar a chave e valor 
meu_dicionariozinho={}

for i in meu_arrayzinho:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i]=1
    else:
        meu_dicionariozinho[i]+=1 

print(meu_dicionariozinho)

#encontrar quem são os valores que aprecem uma unica vez 
#fazer a soma das chaves que aparecem uma unica 1 vez
soma_das_chaves=0
for chave,valor in meu_dicionariozinho.items():
    if valor==1:
        soma_das_chaves+=chave

print(soma_das_chaves)

"""
minha verção 
somador=0
for chave in meu_dicionariozinho:
    if meu_dicionariozinho[chave]==1:
        somador+=chave
print(somador)
"""




