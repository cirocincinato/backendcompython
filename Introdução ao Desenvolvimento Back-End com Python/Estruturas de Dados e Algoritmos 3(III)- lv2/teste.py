def obter_dados_livro(titulo, autor, quantidade):
    return f"{titulo} {autor} {quantidade}"


def obter_quantidade_livro(valor_digitado):
    try:
        quantidade = int(valor_digitado)
        if quantidade >= 0:
            return quantidade
        return "Erro: quantidade não pode ser negativa."
    except ValueError:
        return "Por favor, insira um número válido para a quantidade."


def validar_livro_existe(dicionario_livros, titulo):
    if titulo in dicionario_livros:
        return True
    return f"Erro: O livro '{titulo}' não foi encontrado."


def adicionar_livro(dicionario_livros, titulo, quantidade, autor):
    if validar_livro_existe(dicionario_livros, titulo) is True:
        return f"Erro: o livro '{titulo}' já está cadastrado."
    dicionario_livros[titulo] = {"autor": autor, "quantidade": quantidade}
    return f"Livro '{titulo}' adicionado com sucesso"


def listar_livros(dicionario_livros):
    if not dicionario_livros:
        return "Não há livros cadastrados."
    texto = ""
    for titulo, info in sorted(dicionario_livros.items()):
        texto += f"Título: {titulo} | Autor: {info['autor']} | Quantidade: {info['quantidade']}\n"
    return texto


def remover_livro(dicionario_livros, titulo):
    validacao = validar_livro_existe(dicionario_livros, titulo)
    if validacao is True:
        del dicionario_livros[titulo]
        return f"Livro '{titulo}' removido com sucesso!"
    else:
        return validacao


def atualizar_quantidade(dicionario_livros, titulo, nova_quantidade):
    validacao = validar_livro_existe(dicionario_livros, titulo)
    if validacao is True:
        dicionario_livros[titulo]["quantidade"] = nova_quantidade
        return f"Quantidade de exemplares do livro '{titulo}' atualizada para {nova_quantidade}"
    else:
        return validacao


def obter_quantidade_livro_para_emprestimo(dicionario_livros, titulo, quantidade_str):
    try:
        quantidade = int(quantidade_str)
        if quantidade <= 0:
            return "Erro: quantidade deve ser positiva."
        elif quantidade > dicionario_livros.get(titulo, {}).get("quantidade", 0):
            return "Erro: exemplares insuficientes."
        else:
            return quantidade
    except ValueError:
        return "Erro: digite um número válido."


def registrar_emprestimo(dicionario_livros, historico, titulo, quantidade):
    validacao = validar_livro_existe(dicionario_livros, titulo)
    if validacao is True:
        if dicionario_livros[titulo]["quantidade"] >= quantidade:
            dicionario_livros[titulo]["quantidade"] -= quantidade
            historico.append((titulo, quantidade))
            if quantidade == 1:
                return f"1 exemplar de '{titulo}' emprestado com sucesso!"
            else:
                return f"{quantidade} exemplares de '{titulo}' emprestados com sucesso!"
        else:
            return "Erro: exemplares insuficientes."
    else:
        return validacao


def exibir_historico_emprestimos(historico):
    if not historico:
        return "Não há histórico de empréstimos."
    texto = "Histórico de empréstimos:\n"
    for titulo, quantidade in historico:
        texto += f"{titulo} - {quantidade} exemplar(es)\n"
    return texto


def exibir_menu():
    return (
        "\n===== MENU =====\n"
        "1 - Adicionar livro\n"
        "2 - Listar livros\n"
        "3 - Remover livro\n"
        "4 - Atualizar quantidade\n"
        "5 - Registrar empréstimo\n"
        "6 - Exibir histórico\n"
        "7 - Sair\n"
    )


def menu():
    dicionario_livros = {}
    historico = []

    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ").strip()
            autor = input("Autor: ").strip()
            quantidade = obter_quantidade_livro(input("Quantidade: "))
            if isinstance(quantidade, int):
                print(adicionar_livro(dicionario_livros, titulo, quantidade, autor))
            else:
                print(quantidade)

        elif opcao == "2":
            print(listar_livros(dicionario_livros))

        elif opcao == "3":
            titulo = input("Título do livro a remover: ").strip()
            print(remover_livro(dicionario_livros, titulo))

        elif opcao == "4":
            titulo = input("Título do livro: ").strip()
            quantidade = obter_quantidade_livro(input("Nova quantidade: "))
            if isinstance(quantidade, int):
                print(atualizar_quantidade(dicionario_livros, titulo, quantidade))
            else:
                print(quantidade)

        elif opcao == "5":
            titulo = input("Título do livro: ").strip()
            quantidade_validada = obter_quantidade_livro_para_emprestimo(
                dicionario_livros, titulo, input("Quantidade para empréstimo: ")
            )
            if isinstance(quantidade_validada, int):
                print(registrar_emprestimo(dicionario_livros, historico, titulo, quantidade_validada))
            else:
                print(quantidade_validada)

        elif opcao == "6":
            print(exibir_historico_emprestimos(historico))

        elif opcao == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
