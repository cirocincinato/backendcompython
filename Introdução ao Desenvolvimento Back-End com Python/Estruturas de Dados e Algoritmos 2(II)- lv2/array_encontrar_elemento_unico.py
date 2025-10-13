#dado um array de numeros interiso,cada elemento aparece duas vezes, exceto um. Encontre aquele único

array=[1,1,2,2,4,4,5,5,6,6,7,8,8]
#criar um dicionario para adicionar os valores do array atravez de chave - valor 
#ou seja, a chave sendo o valor do array e o valor sendo a quantidade de vezes que a chave aparece
meu_dicionariozinho={}
for i in array:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i]=1
    else:
        meu_dicionariozinho[i]+=1

print(meu_dicionariozinho)
#fazer a veficação de qual valor aparece uam vez
for chave,valor in meu_dicionariozinho.items():
    if valor==1:
        print(chave)


