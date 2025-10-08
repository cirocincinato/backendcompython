#Tabuada: receber um número e exibir a tabuada de 1 a 10 para ele.

#receber um numero
numero=int(input())

# cria um laso de repetição determinada. como o valor de tabuada que esta sendo pedido é até 10. sabendo disso 
# fiz um for que vai de 1 ate 11, 11 pois o for sempre vai do 0 ate 10-1, para burlar isso usei 10+1=11
#usei a variavel i para multiplicar o valor numero
#range nos da uma sequencia de numeros e sempre botamos um valor a mais do que o que a gente quer. 

for i in range(1,11):
    print("toma",numero*i)