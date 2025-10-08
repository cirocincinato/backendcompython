#aprovado, reprovado,recuperação:
# receba a média de um aluno e diga se ele foi aprovado (media >=(maior ou igual) 7)
# em recuperação (5 <=(maior ou igual a) media <(menor que)7).
# reprovado (media (menor que)<5)

# receba a média

media=float(input())

#aprovado, reprovado,recuperação:
if media>=7:
    print("aprovado")
    
elif (5<=media<7):
    print("recuperação")

# em reprovado (0 <=(maior ou igual a) media <(menor que)5).
elif(0>=media<5):
    print("reprovado")