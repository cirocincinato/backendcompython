"""
Crie um programa que funcione como uma calculadora simples, utilizando 
recursos acessórios do Python. O programa deve seguir os seguintes passos:

Solicite ao usuário que insira dois números para realizar operações 
matemáticas. Caso o usuário insira um valor inválido (como uma letra),
 utilize o gerenciamento de exceções com try-except para exibir uma 
 mensagem de erro e pedir novamente os valores.

Ofereça ao usuário um menu para escolher entre as operações: 
soma, subtração, multiplicação e divisão. 
e o usuário escolher uma operação inválida,
 o programa deve exibir uma mensagem de erro.

Utilize uma função anônima (lambda) para implementar 
cada operação matemática.

Na opção de divisão, verifique se o divisor
 é zero e, caso seja, exiba uma mensagem informando que a 
 divisão por zero não é permitida. Permita que o usuário insira 
 novamente o divisor.

Após realizar a operação escolhida, 
exiba o resultado e pergunte ao usuário se deseja realizar outra operação 
ou encerrar o programa.

Organize o menu de operações usando “list comprehension” 
para exibir as opções numeradas de maneira dinâmica.

Exemplo de Interação:

Insira o primeiro número: 10

Insira o segundo número: 0

Escolha uma operação:

1 - Soma

2 - Subtração

3 - Multiplicação

4 - Divisão

Você escolheu: Divisão

Divisão por zero não é permitida. Por favor, insira outro número: 2

O resultado é: 5.0

Deseja realizar outra operação? (S/N): S

Repita o ciclo até que o usuário decida encerrar.

Como submeter sua entrega

Envie o código no campo de entrega
30mim
"""

def menu():
    menu_txt=["Soma","Subtração","Multiplicação","Divisão"]
    
    menu_numerico=[f"{i+1} - {op}\n" for i,op in enumerate(menu_txt)]

    string=""
    for i in menu_numerico:
        
        string+=i

    return string
def main():

    while True:
        while True:
            try:
                numero0=float(input("Insira o primeiro número: "))
                numero1=float(input("Insira o segundo número: "))
                break
            except ValueError:
                print("Erro: tente novamente")
        print(menu())
        while True:
            option=input()
            meu_dicionariozinho={
                "1": lambda x,y: x+y,
                "2":lambda x,y: x-y,
                "3":lambda x,y:x*y,
                "4":lambda x,y:x/y
            }
            if option in meu_dicionariozinho:
                break
            else:
                print("escolha uma opção valida.")
        while True:
            if option=="4" and numero1==0:
                numero1=float(input("Divisão por zero não é permitida. Por favor, insira outro número: "))
            else:
                break
        print("Resultado da operação: ",meu_dicionariozinho[option](numero0,numero1))
        outra_vez=input("Deseja realizar outra operação? (S/N): ")
        while True:
            if outra_vez=="S" or outra_vez=="N":
                break
            else:
               print(" escolha uma opção valida S para continuar N para encerrar")
        if outra_vez =="N":
            break
            

        

    
main()