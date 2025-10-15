
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
        dicionario_livros_ordenado=dict(sorted(dicionario_livros.items()))
        texto_ordenado=''
        for chave,valor in dicionario_livros_ordenado.items():
            texto_ordenado+=f"título {chave} - {valor['autor']} - {valor['quantidade']}\n"
        return texto_ordenado
        
    
def remover_livro(dicionario_livros,chave_pai_nome_livro):
    if chave_pai_nome_livro in dicionario_livros:
        del dicionario_livros[chave_pai_nome_livro]
        return "livro removido"
    else:
        return "Erro: esse livro não está na base de dados"

def atualizar_quantidade_de_livros(dicionario_livros,chave_pai_nome_livro,valor_filho_quantidade):
    if chave_pai_nome_livro in dicionario_livros:
        dicionario_livros[chave_pai_nome_livro]["quantidade"]=valor_filho_quantidade
        return "Quantidade atualizada."
    else:
        return "Não há histórico de empréstimos."

def registrar_emprestimo(dicionario_livros,historico_emprestimos,chave_pai_nome_livro,valor_filho_quantidade):
    if chave_pai_nome_livro in dicionario_livros:
        #se 'quantidade' do dicioanrio for menor ou igual que a quantidade passada, podemos emprestar livros pois 
        if dicionario_livros[chave_pai_nome_livro]['quantidade']>=valor_filho_quantidade:
            # Subtrai o valor_filho_quantidade da quantidade existente
            dicionario_livros[chave_pai_nome_livro]['quantidade'] -= valor_filho_quantidade
            #para padronizar os valores dentro do array estou definindo que tudo 
            #que for armazenado vai ser string
            historico_emprestimos.append(str(chave_pai_nome_livro))
            historico_emprestimos.append(str(valor_filho_quantidade))
            return "sdfsdfsd"
        else:
            return "Erro exemplares insuficientes"
    else:
        return "Erro esse livro não esta registrado"
def historico_de_emprestio(historico_emprestimos):
    if not historico_emprestimos:
        return "historico vazio"
    else:
        string=''
        cont=0
        #com os valores padronizados é possivel acessar o array, 
        # e criar a estring de 
        # pares ordenados  
        for i in historico_emprestimos:

                cont+=1

                if cont%2==0:
                    string+=f"{i} \n"
                else:
                    string+=f"{i} "

        return string

def exibir_menu():
    return "menu:\n1 - Adicionar livro\n2 - Listar livros\n3 - Remover livro\n4 - Atualizar quantidade de livros\n5 - Registrar empréstimo\n6 - Exibir histórico de empréstimos\n7 - Sair"

def main():
    dicionario_livros={}
    historico_emprestimos=[]
    while True:
        print(exibir_menu())
        option=input("escolha uma opção de 1 a 7: ")
        if option=="1":
            while True: 
                chave_pai_nome_livro=input("nome do licro: ")
                if not chave_pai_nome_livro:
                    print("O campo não pode estar vazio.")
                else:
                    break
            
            while True:
                try:
                    
                    valor_filho_quantidade=int(input("quantidade de exemplares disponíveis: "))
                    break
                except ValueError:
                
                    print("Erro: apenas numeros inteiros")

            while True:
                valor_filho_autor=input("nome do autor: ")
                if not valor_filho_autor:
                    print("O campo não pode estar vazio.")
                else:
                    break
                

            print(adicionar_livro(dicionario_livros,chave_pai_nome_livro,valor_filho_quantidade,valor_filho_autor))
        elif option=="2":
            
            print(listar_livros(dicionario_livros))
        elif option=="3":
            while True: 
                chave_pai_nome_livro=input("nome do livro: ")
                if not chave_pai_nome_livro:
                    print("O campo não pode estar vazio.")
                else:
                    break
            print(remover_livro(dicionario_livros,chave_pai_nome_livro))
        elif option=="4":
            while True: 
                chave_pai_nome_livro=input("nome do livro: ")
                if not chave_pai_nome_livro:
                    print("O campo não pode estar vazio.")
                else:
                    break
            
            while True:
                try:
                    
                    valor_filho_quantidade=int(input("quantidade de exemplares a ser atualizada: "))
                    break
                except ValueError:
                    print("Erro: apenas numeros inteiros")
            print(atualizar_quantidade_de_livros(dicionario_livros,chave_pai_nome_livro,valor_filho_quantidade))
        elif option=="5":
            chave_pai_nome_livro=input("nome do livro: ")
            while True:
                try:
                    valor_filho_quantidade=int(input("quantidade de exemplares do emprestimo: "))
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
            print("Erro: opção invalida. Tente outraz vez!")

main()