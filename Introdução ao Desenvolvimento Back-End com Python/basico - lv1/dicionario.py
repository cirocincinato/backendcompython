#dicionarios retornam erros e eles são muito uteis para fazer tratamento de erros
#isso ajuda a ir direto ao ponto em questoes de logica. como exemplo disso utilizei no exercicio tarefa_de_Estrutura_de_dados.py
#tratando erros que vão ocorrer por padrão dentro de blocos bem definidos.

#informações estão de forma sequencial

lista=[12,324,546,123,876,23453,1,8793453,353457,2342]
#informações estão ligadas uma chave a um valor

meu_dicionario={
    "gato":0,
    "gato2":0,
    "gato3":0,
    "gato4":0,
    "gato45":0
}
#da para passar o lambida no dicioanrio

meu_dicionariozinho={
                "1":(lambda x,y: x+y),
                "2":(lambda x,y: x-y),
                "3":(lambda x,y:x*y),
                "4":(lambda x,y:x/y)
            }
print("meu_dicionariozinho",meu_dicionariozinho['3'](10,10))

for i in lista:
    print(i)

y=0
while y<=5:
    print(y)
    y=y+1

print("valor final da variavel y:", y)
    
my_dict = {'a': 1, 'b': 2}
for key in my_dict:
    print(my_dict[key])
    
tarefas={"correr":True,"andar":False,"sexo":False,"voar":True}
'''
ordenar um dicionário pelas suas chaves em Python, utilize a função sorted() 
aplicada ao método .items() do dicionário, que retorna uma lista de tuplas (chave, valor),
e então especifique a função lambda item: item[0] como o parâmetro key para indicar 
que a ordenação deve ser feita pelo primeiro elemento de cada tupla, que é a chave. 
O resultado pode ser convertido de volta para um dicionário usando dict()
'''
itens_do_dicionario = tarefas.items()

        # Ordena a lista de tuplas pela chave (primeiro elemento de cada tupla)
itens_ordenados = sorted(itens_do_dicionario, key=lambda item: item[0])

        # Converte a lista ordenada de volta para um dicionário
dicionario_ordenado = dict(itens_ordenados)

print("dicionario_ordenado")
