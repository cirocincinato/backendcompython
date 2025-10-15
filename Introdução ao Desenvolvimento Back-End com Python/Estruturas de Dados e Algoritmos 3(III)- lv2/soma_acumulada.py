#dado um array meu_arrayzinho. Definimos uma soma acumulada de um array
#como runninSum[i]=sum(meu_arrayzinho[0]+meu_arrayzinho[i])
#explicação: A soma acumulada é obtida da seguinte forma: [1,1+2,,1+2+3,1+2+3+4]

meu_arrayzinho=[1,2,3,4]

resultado_arrayzinho=[]

cont=0

for numero in meu_arrayzinho:
    cont +=numero
    resultado_arrayzinho.append(cont)

    
print(resultado_arrayzinho)