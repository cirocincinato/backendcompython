#crie um programa que ordene texto para que caber em determinado expasso 
#o programa deve conter daus entardas                   
#sendo entarda_de_exemplo=str
# texto_a_ser_convertido=srt
# 
# chave valor 
# 
# 
# 
def p(parametro_qualquer):
    print(parametro_qualquer)

def padronizar_texto(texto_tamanho_de_exemplo,texto_texto_completo):
    print(texto_tamanho_de_exemplo)

def identidicar_quantidade(variavel_str_tartamentos):
    tamanho=len(texto_texto_completo)
    
    def s():
        print()
    s()

    
def menu():
    while True:
        global option
        print("Menu:\n"
              "1 - padronizar texto\n"
              "2 - Identidicar quantidade de \n carcateres em variavel=str\n"
              "3 - Remover produto\n"
              "4 - Atualizar quantidade de produto\n"
              "5 - Sair")
        option=input("opção:")

        if option=="1":
            texto_tamanho_de_exemplo="Recentemente Sr. Miranda, um dos contadores da ACM"
            texto_texto_completo=" percebeu que a máquina apresentava falha em um, e apenas um, dos dígitos numéricos. Mais especificamente, o dígito falho, quando datilografado, não é impresso na folha, como se a tecla correspondente não tivesse sido pressionada. Ele percebeu que isso poderia ter alterado os valores numéricos representados nos contratos e, preocupado com a contabilidade, quer saber, a partir dos valores originais negociados nos contratos, que ele mantinha em anotações manuscritas, quais os valores de fato representados nos contratos. Por exemplo, se a máquina apresenta falha no dígito 5, o valor 1500 seria datilografado no contrato como 100, pois o 5 não seria impresso. Note que o Sr. Miranda quer saber o valor numérico representado no contrato, ou seja, nessa mesma máquina, o número 5000 corresponde ao valor numérico 0, e não 000 (como ele de fato aparece impresso)."
            

            print(identidicar_quantidade(texto_texto_completo))
            print(padronizar_texto(texto_tamanho_de_exemplo,texto_texto_completo))
        elif option=="2":
            texto_texto_completo=" percebeu que a máquina apresentava falha em um, e apenas um, dos dígitos numéricos. Mais especificamente, o dígito falho, quando datilografado, não é impresso na folha, como se a tecla correspondente não tivesse sido pressionada. Ele percebeu que isso poderia ter alterado os valores numéricos representados nos contratos e, preocupado com a contabilidade, quer saber, a partir dos valores originais negociados nos contratos, que ele mantinha em anotações manuscritas, quais os valores de fato representados nos contratos. Por exemplo, se a máquina apresenta falha no dígito 5, o valor 1500 seria datilografado no contrato como 100, pois o 5 não seria impresso. Note que o Sr. Miranda quer saber o valor numérico representado no contrato, ou seja, nessa mesma máquina, o número 5000 corresponde ao valor numérico 0, e não 000 (como ele de fato aparece impresso)."
            

            

        elif option=="3":
            p("...")
        elif option=="4":
            p("...")
        elif option=="5":
            p("Saindo...")
            break
        else:
            p("escolha uma opção valida")

def main():
    global entrada_de_exemplo
    global meu_dicionario
    entrada_de_exemplo="Recentemente Sr. Miranda, um dos contadores " \
    "da ACM, p"
    meu_dicionario={}
    entrada_de_exemplo_contada=len(entrada_de_exemplo)
    menu()


main()