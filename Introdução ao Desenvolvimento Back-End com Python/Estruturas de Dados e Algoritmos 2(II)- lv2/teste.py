dados_produto = {"func01": {
        "quant": 100,
        "valor": 100
    },
    "func02": {
        "quant": 100,
        "valor": 100
    },
    "bolas": {
        "quant": 100,
        "valor": 1.4
    }
    }

dados_ordenados = dict(sorted(dados_produto.items(), key=lambda item: item[0]))
for produto, info in dados_ordenados.items():
    print(f"Nome do produto: {produto} — Quantidade disponível: {info['quant']} — Preço: R${info['valor']:.2f}")



'''

#caso dicionario vazio vou adicionar os valores
if len(dados_produto)==0:
        print("caso dicionario vazio adiciona de imediato")
        dados_produto[x] = {
            "quant": y,
            "valor": z
        }
        print(dados_produto)
#se ele não estiver vazio vou iniciar um for verificando se a chave é igual ao produto que quero adicionar
else:
    for chave,valor in dados_produto.items():
        cont+=1
        if chave!=x and cont==len(dados_produto):   
            print("adiciona no dicionario caso chave seja difernte de produto e meu for chegou ao fim ")
            dados_produto[x] = {
                "quant": y,
                "valor": z
            }
            print(dados_produto)
        elif chave==x:
            print("esta no dicioanrio")

# Dicionário externo
funcionarios = {}

# Adicionando um novo funcionário com seu dicionário de detalhes
funcionarios[x] = {
    "quant": y,
    "valor": z
}

print(funcionarios)'''