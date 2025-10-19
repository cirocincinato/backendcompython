'''

tarefas={'c': {'autor': '123', 'quantidade': 123}, 'b': {'autor': '2', 'quantidade': 123}, 'a': {'autor': '1', 'quantidade': 12}}
itens_do_dicionario = tarefas.items()

        # Ordena a lista de tuplas pela chave (primeiro elemento de cada tupla)
itens_ordenados = sorted(itens_do_dicionario, key=lambda item: item[0])

        # Converte a lista ordenada de volta para um dicionário
dicionario_ordenado = dict(itens_ordenados)

print("dicionario_ordenado")
'''
##
##suposta mente essa é a melhor solução apos minahs pesquisas
dicionario_livros={'a': {'autor': '123', 'quantidade': 123}, 'b': {'autor': '11', 'quantidade': 111}, 'c': {'autor': '123', 'quantidade': 123}}
dicionario_livros_ordenado = dict(
    sorted(dicionario_livros.items(), key=lambda item: item[0])
)
resultado = "\n".join(
    f"{chave} - {valor['autor']} - {valor['quantidade']}"
    for chave, valor in dicionario_livros_ordenado.items()
)
#faz a mesma coisa mas não cria o resultado espetrado que é o print
tarefas={'c': {'autor': '123', 'quantidade': 123}, 'b': {'autor': '2', 'quantidade': 123}, 'a': {'autor': '1', 'quantidade': 12}}
itens_do_dicionario = tarefas.items()
print(itens_do_dicionario)
        # Ordena a lista de tuplas pela chave (primeiro elemento de cada tupla)
itens_ordenados = sorted(itens_do_dicionario)
print(itens_ordenados)
        # Converte a lista ordenada de volta para um dicionário
dicionario_ordenado = dict(itens_ordenados)

print(dicionario_ordenado)