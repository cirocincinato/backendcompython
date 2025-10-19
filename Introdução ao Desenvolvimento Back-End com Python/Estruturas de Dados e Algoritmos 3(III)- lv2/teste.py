def adicionar_livro(dicionario_livros, titulo, quantidade, autor):
    if titulo not in dicionario_livros:
        dicionario_livros[titulo] = {
            "autor": autor,
            "quantidade": quantidade
        }
        return f"Livro '{titulo}' adicionado com sucesso"
    else:
        return f"Erro: o livro '{titulo}' já está cadastrado."


def listar_livros(dicionario_livros):
    if not dicionario_livros:
        return "Não há livros cadastrados."
    else:
        dic_ordenado = dict(sorted(dicionario_livros.items(), key=lambda item: item[0]))
        listagem = "\n".join(f"{titulo} - {dados['autor']} - {dados['quantidade']}" for titulo, dados in dic_ordenado.items())
        return listagem


def remover_livro(dicionario_livros, titulo):
    if titulo in dicionario_livros:
        del dicionario_livros[titulo]
        return f"Livro '{titulo}' removido com sucesso."
    else:
        return f"Erro: o livro '{titulo}' não foi encontrado."


def atualizar_quantidade(dicionario_livros, titulo, nova_quantidade):
    if titulo in dicionario_livros:
        dicionario_livros[titulo]["quantidade"] = nova_quantidade
        return f"Quantidade de exemplares do livro '{titulo}' atualizada para {nova_quantidade}"
    else:
        return f"Erro: o livro '{titulo}' não foi encontrado."


def registrar_emprestimo(dicionario_livros, historico_emprestimos, titulo, quantidade):
    if titulo in dicionario_livros:
        if dicionario_livros[titulo]["quantidade"] >= quantidade:
            dicionario_livros[titulo]["quantidade"] -= quantidade
            historico_emprestimos.append((titulo, quantidade))
            return f"{quantidade} exemplar(es) de '{titulo}' emprestado(s) com sucesso!"
        else:
            return "Erro: exemplares insuficientes."
    else:
        return f"Erro: o livro '{titulo}' não foi encontrado."


def historico_de_emprestimo(historico_emprestimos):
    if not historico_emprestimos:
        return "Não há histórico de empréstimos."
    else:
        texto = "Histórico de empréstimos:\n"
        for titulo, quantidade in historico_emprestimos:
            texto += f"{titulo} - {quantidade} exemplar(es)"
        return "\n".join(texto)


def exibir_menu():
    return (
        "Menu:\n"
        "1 - Adicionar livro\n"
        "2 - Listar livros\n"
        "3 - Remover livro\n"
        "4 - Atualizar quantidade de livros\n"
        "5 - Registrar empréstimo\n"
        "6 - Exibir histórico de empréstimos\n"
        "7 - Sair"
    )


def main():
    dicionario_livros = {}
    historico_emprestimos = []

    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção de 1 a 7: ")

        if opcao == "1":
            titulo = input("Título do livro: ").strip()
            if not titulo:
                print("Erro: o título não pode estar vazio.")
                continue

            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Erro: apenas números inteiros são aceitos.")
                continue

            autor = input("Autor: ").strip()
            if not autor:
                print("Erro: o autor não pode estar vazio.")
                continue

            print(adicionar_livro(dicionario_livros, titulo, quantidade, autor))

        elif opcao == "2":
            print(listar_livros(dicionario_livros))

        elif opcao == "3":
            titulo = input("Título do livro a remover: ").strip()
            print(remover_livro(dicionario_livros, titulo))

        elif opcao == "4":
            titulo = input("Título do livro: ").strip()
            if not titulo:
                print("Erro: o título não pode estar vazio.")
                continue
            try:
                nova_quantidade = int(input("Nova quantidade: "))
            except ValueError:
                print("Erro: apenas números inteiros são aceitos.")
                continue

            print(atualizar_quantidade(dicionario_livros, titulo, nova_quantidade))

        elif opcao == "5":
            titulo = input("Título do livro: ").strip()
            if not titulo:
                print("Erro: o título não pode estar vazio.")
                continue
            try:
                quantidade = int(input("Quantidade para empréstimo: "))
            except ValueError:
                print("Erro: apenas números inteiros são aceitos.")
                continue

            print(registrar_emprestimo(dicionario_livros, historico_emprestimos, titulo, quantidade))

        elif opcao == "6":
            print(historico_de_emprestimo(historico_emprestimos))

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Erro: opção inválida. Tente novamente!")


main()
