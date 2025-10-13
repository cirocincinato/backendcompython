meu_arrayzinho=[elemento for elemento in range(1,6)]
print(meu_arrayzinho)


palavras=["paython","é","divertido"]
iniciais =[palavra[0] for palavra in palavras]
print(iniciais)

#1 2 3 4 5 6 7 8 9 10

#1 4 9 16 25 36 49 64 81 100 

quadrados_impares =[elemento**2 for elemento in range(1,11) if elemento%2 !=0]
print(quadrados_impares)

#A função enumerate() do Python ajuda você com loops que exigem um contador, 
#adicionando um índice a cada item em um iterável. 
#Isso é particularmente útil quando você precisa do índice e do valor durante a
#iteração, como ao listar itens com suas posições.
menu_txt=["Soma","Subtração","Multiplicação","Divisão"]
menu_numerico=[f"{i+1} - {op}" for i,op in enumerate(menu_txt)]
print(menu_numerico)