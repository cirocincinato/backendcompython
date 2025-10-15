#retone a media de todos os salarios, com exceção do maior e menor

salary=[4000,3000,1000,2000,5000,500]
#ordeno os valores 
novo_arrayzinho=sorted(salary)
print(novo_arrayzinho)
novo_arrayzinho.remove(novo_arrayzinho[0])
novo_arrayzinho.remove(novo_arrayzinho[-1])

media_dos_salarios=0

for salario in novo_arrayzinho:
    media_dos_salarios+=salario

print(media_dos_salarios//len(novo_arrayzinho))