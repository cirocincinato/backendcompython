#dado um array inteiro meu_arrayzinho, retorne verdadeiro se 
# algum valor aparecer pelo menos duas vezes no array
#e retorne falso se cada elemento for distinto. 

meu_arrayzinho=[1,1,1,3,3,4,3,2,4,2]

meu_dicionariozinho={}

for valor_indice in meu_arrayzinho:
    if valor_indice not in meu_dicionariozinho:
        meu_dicionariozinho[valor_indice]=1
    else:
        meu_dicionariozinho[valor_indice]+=1

for chave,valor in meu_dicionariozinho.items():

    if valor>=2:
        print(True)
        
    else:
        print(False)

