#dado um array de números inteitos, retorne a soma do menor números e do maior números do array.

meu_arrayzinho=[1,34,4,5,67,8,9,4,100]

#vamor ordenar o array para deixar o menor valor na posição zero do array
#e o maior valor na ultima posição do array

meu_arrayzinho.sort()

#efetuar a soma do valor que está na ultima posição ao valor que está na primera posição do array 

primeiro_valor=meu_arrayzinho[0]
ultimo_valor=meu_arrayzinho[-1]


print(primeiro_valor+ultimo_valor)