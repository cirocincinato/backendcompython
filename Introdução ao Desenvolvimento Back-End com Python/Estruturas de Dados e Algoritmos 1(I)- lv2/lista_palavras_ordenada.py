#Receba uma lista de palavras e ordene elas de forma alfabetica

#Receba uma lista ['ciro', 'lucas', 'amasr', 'fder', 'valentine']
arrey_palavras=[]

#definir quantidade: vai ser 5(5+1)
#logica para recebr e adicionar palvras no arrey
for i in range(1,6):
    arrey_palavras.append(input())

#ordenar a lista
arrey_palavras.sort()
print(arrey_palavras)
'''
 A função sorted() é uma função embutida que pode ser usada com qualquer tipo de iterável
(como listas, tuplas e dicionários). Ela retorna uma nova lista com os elementos ordenados,
 deixando a lista original inalterada.
Exemplo:
python
'''
lista_original = [3, 1, 4, 1, 5, 9, 2]
nova_lista = sorted(lista_original)
print(lista_original) # Saída: [3, 1, 4, 1, 5, 9, 2]
print(nova_lista) # Saída: [1, 1, 2, 3, 4, 5, 9]