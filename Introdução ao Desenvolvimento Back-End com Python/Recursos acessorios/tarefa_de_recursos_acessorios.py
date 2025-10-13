def menu():
    opcoes=["Soma","Subtração", "Multiplicação", "Divisão"]
    menu_numerado=[f"{i+1} - {op}" for i,op in enumerate(opcoes)]
    return "\n".join(menu_numerado)
def main():
    while True:
        while True:
            try:
                numero0 = float(input("Insira o primeiro número: "))
                numero1 = float(input("Insira o segundo número: "))
                break
            except ValueError:
                print("Erro: valor inválido. Por favor, insira um número válido.")
        print("\nMenu")
        print(menu())
        opcao=input("\nDigite o número da operação desejada: ")
        operacoes = {
            "1": ("Soma", lambda x, y: x + y),
            "2": ("Subtração", lambda x, y: x - y),
            "3": ("Multiplicação", lambda x, y: x * y),
            "4": ("Divisão", lambda x, y: x / y if y != 0 else None)
        }
        if opcao not in operacoes:
            print("Erro: operação inválida. Tente novamente.\n")
            continue
        # ✅ Tratamento especial para divisão por zero
        if opcao == "4" and numero1 == 0:
            while True:
                try:
                    numero1 = float(input("Divisão por zero não é permitida. Por favor, insira outro número: "))
                    if numero1 != 0:
                        break
                except ValueError:
                    print("Erro: valor inválido. Insira um número válido.")
        nome_operacao, funcao = operacoes[opcao]
        # ✅ Calcula e exibe o resultado
        resultado = funcao(numero0, numero1)
        print(f"\nO resultado é: {resultado}\n")

        # ✅ Pergunta se o usuário quer continuar
        while True:
            novamente = input("Deseja realizar outra operação? (S/N): ").strip().upper()
            if novamente in ("S", "N"):
                break
            else:
                print("Opção inválida. Digite S ou N.")

        if novamente == "N":
            print("Encerrando o programa. Até mais!")
            break


if __name__ == "__main__":
    main()