x=[
    {"nome_tarefa":"corrida pela manha","descricao":"correr bastante de das 6a.m até 10 a.m","concluido":False},
    {"nome_tarefa":"caminhada noturna","descricao":"correr bastante de das 9p.m até 11p.m","concluido":False},
    {"nome_tarefa":"resa para DEUS","descricao":"horar para o pai supremo","concluido":False},
    {"nome_tarefa":"tempo de qualida","descricao":"py aula5.py","concluido":False}
]
#GET 
print(len(x))

#POST
nome_nova="SEXO matinal"
descricao_nova="SEXO deve ser feito todos os dias"
x.append({"nome_tarefa":descricao_nova,"descricao":nome_nova,"concluido":False})
print(x)

#vamos adicionar informaçoes para a tabela
#seria a libha da tabela 
#PUT
for linha in x:
    if linha["nome_tarefa"]=="resa para DEUS":
        linha["concluido"]=True
        print(linha)

for linha in x:
    if linha["nome_tarefa"]=="caminhada noturna":
        x.remove(linha)
print(x)
        
        

