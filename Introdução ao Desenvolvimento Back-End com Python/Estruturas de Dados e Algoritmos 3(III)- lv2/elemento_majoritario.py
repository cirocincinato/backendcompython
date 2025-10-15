#dado um array de tamanho n, retorne o elemento majoritario.
#o elemento majoritário é aquele que aparece mais de [n/2] vezes.
#você pode assumir que o elemento majoritário sempre existe no array

meu_arrayzinho=[3,2,3]

#majoritário é aquele que aparece mais de [n/2]
n=len(meu_arrayzinho)

item_majoritario=(n/2)

meu_dicionariozinho={}
contador=0
for i in meu_arrayzinho:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i]=1
    else:
        meu_dicionariozinho[i]+=1

for chave,valor in meu_dicionariozinho.items():
    if valor>=item_majoritario:
        print("       ",chave)