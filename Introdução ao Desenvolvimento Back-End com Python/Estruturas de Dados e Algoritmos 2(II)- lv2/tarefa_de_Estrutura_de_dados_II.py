#Crie um programa para gerenciar um estoque de produtos. 
# O programa deve exibir um menu com as opções: 
# adicionar produto, listar produtos, remover produto,
# atualizar quantidade de produto e sair do programa.

#Utilize um dicionário para armazenar os produtos. Cada produto será uma chave no dicionário, 
# e o valor será outro dicionário contendo duas chaves: "quantidade" (indicando a quantidade disponível) 
# e "preço" (o preço do produto).

dados_produtos={}


def adicionar_produto(produto,quantidade,preco):
    global dados_produtos
    if produto not in dados_produtos:
        dados_produtos[produto]={

            "quantidade":quantidade ,

            "valor":preco
            }
        return ""
    
    else:
        return "esse produto ja existe"
def listar_produtos():
    global dados_produtos

    dados_ordenados = dict(sorted(dados_produtos.items(), key=lambda item: item[0]))

    resultado = ""
    for produto, info in dados_ordenados.items():
        resultado += f"{produto}: {info['quantidade']} — {info['valor']:.2f}\n"
    return resultado
    
def remover_produto(produto):
    global dados_produtos
    if produto not in dados_produtos:

        return "Erro:esse produto não existe"
    else:
        del dados_produtos[produto]
        return "removido"
    
def atualizar_quantidade_produto(produto,quantidade):
        
    global dados_produtos
    
    if produto in dados_produtos:
        dados_produtos[produto]["quantidade"] = quantidade
        return "atualizado"
    else:
        return f"Erro: o produto '{produto}' não foi encontrado."
    
def menu():
    while True:
        print("Menu:\n"
              "1 - Adicionar produto\n"
              "2 - Listar produtos\n"
              "3 - Remover produto\n"
              "4 - Atualizar quantidade de produto\n"
              "5 - Sair")
        opcao=input("informa um valor numerico corespondente a opçaõ desejada:")

        if opcao=="1":

            produto=input("informe o nome do produto:")

            quantidade=float(input("informe a quantidade disponivel(apenas numeros são aceitos):"))

            preco=float(input("informe o preço(apenas numeros são aceitos):"))

            print(adicionar_produto(produto,quantidade,preco))

        elif opcao=="2":
            print(listar_produtos())

        elif opcao=="3":
            produto=input("informe o nome do produto:")

            print(remover_produto(produto))
        elif opcao=="4":
            
            produto=input("informe o nome do produto:")
            quantidade=float(input("informe a quantidade disponivel(apenas numeros são aceitos):"))

            print(atualizar_quantidade_produto(produto,quantidade))
        elif opcao=="5":
            break
        else:
            print("selecione uma opção valida.")
def main():
    global dados_produtos
    menu()

if __name__ == "__main__":
    main()