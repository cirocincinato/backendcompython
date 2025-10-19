# Lista de convidados VIP (pode ser modificada nos testes)
convidados_vip = ["Alice", "Bob", "Carol"]

# Função para verificar se a idade permite entrada
def verificar_idade(idade):
    if idade >= 18:
        return "Entrada permitida. Bem-vindo ao evento!"
    else:
        return "Entrada negada. Este evento é apenas para maiores de idade."

# Função para verificar se o nome está na lista VIP
def verificar_vip(nome):
    if nome in convidados_vip:
        return "Você é um convidado VIP! Aproveite o evento com acesso especial."
    else:
        return None

# Programa principal