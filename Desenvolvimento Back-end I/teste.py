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


#as clases intermediaruias migrariam para as clasese
#  primordiarias(topo da poramidis .) 
d=0
print(d)