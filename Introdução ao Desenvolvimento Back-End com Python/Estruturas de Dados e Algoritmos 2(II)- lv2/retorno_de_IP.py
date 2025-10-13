#dado um endereço IP válido(IPv4), retorne uma versão ajustada desse endereço IP
#Um endereço IP ajustado substitui cada ponto "." por "[.]"

#ip="1.1.1.1"
#versão ajustada_ip="1[.]1[.]1[.]1"


#receber a string com nosso endereço IP
endereco_ip="1.1.1.1"

#fazer a operação para substituir os pontos por parenteses e ponto

#correr dentro da string. então criamos uma nova estring parar armazenar essa nova string
#fazer a operação para substituir os .(pontos) por [.](parenteses e ponto)
novo_endereco_ip=""


for i in endereco_ip:
    if i == ".":
        novo_endereco_ip += "[.]"
    else:
        novo_endereco_ip+=i
    
print("resultado final",novo_endereco_ip)