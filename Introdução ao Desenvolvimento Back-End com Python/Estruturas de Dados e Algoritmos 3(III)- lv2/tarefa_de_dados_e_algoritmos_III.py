
def adicionar_livro(dicionario_livros,chave_pai_nome_livro,valor_filho_quantidade,valor_filho_autor):
    if chave_pai_nome_livro not in dicionario_livros:
        dicionario_livros[chave_pai_nome_livro]={
            "autor":valor_filho_autor,
            "quantidade":valor_filho_quantidade}
        return f"Livro {chave_pai_nome_livro} adicionado com sucesso"
    else:
        return(f"esse livro({chave_pai_nome_livro}) já está adicionada")
    
def listar_livros(dicionario_livros):
    if not dicionario_livros:
        return "Não há livros cadastrados."
    else:
        dic_ordenado=dict(sorted(dicionario_livros.items(), key=lambda valor_da_tupla:valor_da_tupla[0]))
        listagem_de_livros_em_str="\n".join(f"{chave} - {valor['autor']} - {valor['quantidade']}" for chave,valor in dic_ordenado.items())
        return listagem_de_livros_em_str
    
def remover_livro(dicionario_livros,chave_pai_nome_livro):
    if chave_pai_nome_livro in dicionario_livros:
        del dicionario_livros[chave_pai_nome_livro]
        return f"{chave_pai_nome_livro} removido"
    else:
        return f"Erro: O livro '{chave_pai_nome_livro}' não foi encontrado."

def atualizar_quantidade_de_livros(dicionario_livros,chave_pai_nome_livro,valor_filho_quantidade):
    if chave_pai_nome_livro in dicionario_livros:
        dicionario_livros[chave_pai_nome_livro]["quantidade"]=valor_filho_quantidade
        return f"Quantidade de exemplares do livro '{chave_pai_nome_livro}' atualizada para {valor_filho_quantidade}"
    else:
        return f"Erro: O livro '{chave_pai_nome_livro}' não foi encontrado."

def registrar_emprestimo(dicionario_livros,historico_emprestimos,chave_pai_nome_livro,valor_filho_quantidade):
    if chave_pai_nome_livro in dicionario_livros:
        #se 'quantidade' do dicioanrio for menor ou igual que a quantidade passada, podemos emprestar livros pois 
        if dicionario_livros[chave_pai_nome_livro]['quantidade']>=valor_filho_quantidade:
            # Subtrai o valor_filho_quantidade da quantidade existente
            dicionario_livros[chave_pai_nome_livro]['quantidade'] -= valor_filho_quantidade
            #para padronizar os valores dentro do array estou definindo que tudo 
            #que for armazenado vai ser string
            historico_emprestimos.append((chave_pai_nome_livro,valor_filho_quantidade))
            return f"{chave_pai_nome_livro} - número de exemplares emprestados: {valor_filho_quantidade}"
        else:
            return "Erro exemplares insuficientes"
    else:
        return f"Erro: O livro '{chave_pai_nome_livro}' não foi encontrado."
def historico_de_emprestio(historico_emprestimos):
    if not historico_emprestimos:
        return "Não há histórico de empréstimos."
    else:
        texto = "Histórico de empréstimos:\n"
#listagem_de_livros_em_str="\n".join(f"{chave} - {valor['autor']} - {valor['quantidade']}" for chave,valor in dic_ordenado.items())
        texto_final="\n".join(f"{livro} - {quantidade} exemplar(es)" for livro,quantidade in historico_emprestimos)
        return texto+texto_final
def exibir_menu():
    return "menu:\n1 - Adicionar livro\n2 - Listar livros\n3 - Remover livro\n4 - Atualizar quantidade de livros\n5 - Registrar empréstimo\n6 - Exibir histórico de empréstimos\n7 - Sair"
    #return "---escolha----:"
def main():
    dicionario_livros={}
    historico_emprestimos=[]
    while True:
        #print(dicionario_livros)
        print(exibir_menu())
        option=input("escolha uma opção de 1 a 7: ")
        if option=="1":
            while True: 
                chave_pai_nome_livro=input("Título do livro: ")
                if not chave_pai_nome_livro:
                    print("O campo não pode estar vazio.")
                else:
                    break
            
            while True:
                try:
                    
                    valor_filho_quantidade=int(input("Quantidade: "))
                    break
                except ValueError:
                
                    print("Erro: apenas numeros inteiros")

            while True:
                valor_filho_autor=input("Autor: ")
                if not valor_filho_autor:
                    print("O campo não pode estar vazio.")
                else:
                    break
                

            print(adicionar_livro(dicionario_livros,chave_pai_nome_livro,valor_filho_quantidade,valor_filho_autor))
        elif option=="2":
            
            print(listar_livros(dicionario_livros))
        elif option=="3":
            while True: 
                chave_pai_nome_livro=input("Título do livro a remover: ")
                if not chave_pai_nome_livro:
                    print("O campo não pode estar vazio.")
                else:
                    break
            print(remover_livro(dicionario_livros,chave_pai_nome_livro))
        elif option=="4":
            while True: 
                chave_pai_nome_livro=input("Título do livro: ")
                if not chave_pai_nome_livro:
                    print("O campo não pode estar vazio.")
                else:
                    break
            
            while True:
                try:
                    
                    valor_filho_quantidade=int(input("Nova quantidade: "))
                    break
                except ValueError:
                    print("Erro: apenas numeros inteiros")
            print(atualizar_quantidade_de_livros(dicionario_livros,chave_pai_nome_livro,valor_filho_quantidade))
        elif option=="5":
            chave_pai_nome_livro=input("Título do livro: ")
            while True:
                try:
                    valor_filho_quantidade=int(input("Quantidade para empréstimo: "))
                    break
                except ValueError:
                    print("Erro: apenas numeros inteiros")
            print(registrar_emprestimo(dicionario_livros,historico_emprestimos,chave_pai_nome_livro,valor_filho_quantidade))
        elif option=="6":

            print(historico_de_emprestio(historico_emprestimos))
        elif option=="7":

            print("saindo...")
            break
        else:
            print("Erro: Opção invalida. Tente outraz vez!")

main()
