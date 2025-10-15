#definimos o uso de letra maiúsculas em uma plavra como correto quando o 
# seguinte caso é válido:

#todas as letras desta palavra são MAIÚSCULAS, como "EUA"

#dada uma palavra de string, retone verdadeiro se o uso de letras maiúsculas 
#está correto

stringzinha="CACHORRO"

cont=0

for letras in stringzinha:
    if letras.isupper():
        cont+=1

if cont==len(stringzinha):
    print("é uma STRING COM LETRAS MAIÚSCULAS")
else:
    print("tem letras minúsculas nessa string")