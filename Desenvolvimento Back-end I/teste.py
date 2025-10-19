'''
tarefas = []
tarefas1 = []
if not tarefas1:
    print("não tem terefa")

# Exemplo de como adicionar tarefas à lista.
tarefas.append({
    'nome': 'Ir ao supermercado',
    'descricao': 'Comprar frutas, verduras, leite e pão.',
    'concluida': False
})

tarefas.append({
    'nome': 'Pagar contas',
    'descricao': 'Quitar as contas de água, luz e internet.',
    'concluida': False
})

tarefas.append({
    'nome': 'Estudar Python',
    'descricao': 'Assistir às aulas online sobre dicionários e listas.',
    'concluida': False
})

#se id for maior(>)ou igual que tarefa então não existe na lista
id=-1
if id >= len(tarefas):
    print("esse id não existe")
else:
    print(tarefas[id])

'''
#as clases intermediaruias migrariam para as clasese
#  primordiarias(topo da poramidis .) 

#lista_com_dic=[{'tarefa1': {'descricao': 'correr dia 1', 'concluida': False}}, {'tarefa2': {'descricao': 'correr1', 'concluida': False}}, {'tarefa3': {'descricao': 'correr2', 'concluida': False}}]

###POST 
tarefas=[{}]
x=any(tarefas)
print(x)
while True:
    x=input("1.add 2.sair")
    if x=="1":
        
        id_tarefa=int(input())
        nome_tarefa=input("nome ")
        descricao_tarefa=input("descri ")
        ###POST 1
        #se tarefa estiver vazia e o id for igual a 0 
        id_existe = any(id_tarefa in d for d in tarefas)

            # Verificar se o nome já existe
        nome_existe = any(
                    dados['nome_tarefa'] == nome_tarefa
                    for item in tarefas
                    for dados in item.values()
                )
        if id_existe==False and nome_existe==False:
                tarefas.append({
                        id_tarefa: {
                            'nome_tarefa': nome_tarefa,
                            'descricao': descricao_tarefa,
                            'concluida': False
                        }
                    })
        
        print(len(tarefas))
    elif x=="2":
         break
'''
try:
    if id_tarefa in lista_com_dic[id_tarefa]:
        x="erro:pois id_tarefa não existe na lista"
except IndexError:
        print("Não existe nenhuma tarefa. ENTÃO VAMOS ADICIOANAR")
        lista_com_dic.append({id_tarefa:{
            'nome_tarefa': "andar",
            'descricao': "andarrrr",
            'concluida': False
        }})

print(lista_com_dic)'''