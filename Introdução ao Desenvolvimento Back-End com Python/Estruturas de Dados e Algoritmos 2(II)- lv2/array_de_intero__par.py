#dado um array de números inteiros, retorne quantos deles contêm um número par de dígitos.
nums=[12,345,2,6,7896,6511,1651541,165498741231651,118911451,1841214,111,1,1,1,1,1,11,1,1,11,11,1]


# Usando list comprehension para converter cada número em string
novo_array_convertido = [str(num) for num in nums]
print(novo_array_convertido)

#novo_nums=['12','345','2','6','7896'] novas estrings

#converter para string é bom. CONVERTER NO GERAL
#PENSAMENTO LOGICO: 
#criar um novo array de strings que vai ter os mesmos valores do primero array, 
# porem como strings

novo_nums=['12','345','2','6','7896']

#fazer um looping dentro do novo_array para fazer a verificação dde números com digitos pares

#fazer a contagem e mostrar (printar) na tela o resultado
contador=0
for i in novo_nums:
    if len(i)%2==0:
        contador+=1
    else:
        print("não")

print(contador, ": retorne quantos deles contêm um número par ")

