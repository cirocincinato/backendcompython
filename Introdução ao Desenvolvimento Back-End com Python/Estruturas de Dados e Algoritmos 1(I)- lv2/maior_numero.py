#escreva um programa que receba numeros e diga qual é o segundo maior numero

#receber numeros 
numero0,numero1,numero2,numero3,numero4=map(int,input().split())

#criar uma logica para ver quem é o segundo maior

array=[]
array.append(numero0)
array.append(numero1)
array.append(numero2)
array.append(numero3)
array.append(numero4)

#ordena os numeros
array.sort()
print(array)
#pega um valor antes do valor final= como a lista esta agora ordenada e so pegar valor final-2=segundo maior

final=len(array)
print(final)
#mostrar o segundo maior valor 

print(array[final-2])

#ou dessa forma tambe funfa 
numbers = [3, 1, 4,5,67,878,567]
numbers.sort()
print(numbers)
second_largest = numbers[-2]
print(second_largest)
