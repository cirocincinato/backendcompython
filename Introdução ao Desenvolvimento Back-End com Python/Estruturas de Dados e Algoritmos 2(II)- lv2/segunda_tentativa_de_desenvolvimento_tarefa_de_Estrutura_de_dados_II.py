def adicionar_produto():
    chave_pai=input()
    if chave_pai not in estrutura_de_Dados:
        valor_filho_quantidade=int(input())
        valor_filho_preco=float(input())
        estrutura_de_Dados[chave_pai]={
            'quantidade':valor_filho_quantidade,
            'preco':valor_filho_preco
        }
    else:
        return f"erro, pois esse produto ja existe{chave_pai}"
    return "adicionado ao estoque" 
def listar_produtos():
    string=""
    for chave,valor in sorted(estrutura_de_Dados.items(),key=lambda item:item[0]):
        string+=f"\n{chave} e {valor['quantidade']} - {valor['preco']}\n"
    return string
def remover_produto():
    chave_pai=input("remover:")
    if chave_pai in estrutura_de_Dados:
        del estrutura_de_Dados[chave_pai]
        return f"Produto '{chave_pai}' removido com sucesso!"
    else:
        return "Erro: Produto não encontrado."
    
def atualizar_produto():
    chave_pai=input()
    if chave_pai in estrutura_de_Dados:
        valor_filho_quantidade=int(input())
        valor_filho_preco=float(input())
        estrutura_de_Dados[chave_pai]={
            'quantidade':valor_filho_quantidade,
            'preco':valor_filho_preco
        }
    else:
        return "Erro: Produto não encontrado."
    return f"atualizado:{chave_pai}"
def main():
    global estrutura_de_Dados
    estrutura_de_Dados={}
    while True:
        print("Menu segunda versão:\n"
              "1 - Adicionar produto\n"
              "2 - Listar produtos\n"
              "3 - Remover produto\n"
              "4 - Atualizar quantidade\n"
              "5 - Sair")
        option=input("opção: ")
# print(type(variavel))       
        if option=="1":
            
            print(adicionar_produto())

        elif option=="2":
            print(listar_produtos())
        elif option=="3":
            print(remover_produto())
        elif option=="4":
            print(atualizar_produto())
        elif option=="5":
            print("saindo...")
            break
        else:
            print("valor valido porfa")
if __name__ == "__main__":
    main()


