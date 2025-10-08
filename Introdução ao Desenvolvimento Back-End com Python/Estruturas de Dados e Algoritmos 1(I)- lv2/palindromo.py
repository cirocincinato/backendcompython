#receba um numero e determine se ele é palindromo(lê-se igual de frente pra trás exemplo: 191,232,11)

#receber numero 

numero=int(input())

#determinar se é 
#primero tranformo o numero(int) em string(str)
string_numero=str(numero)

#utilizando a função de conversão, que deixa uma string de tras pra frente. podemos usar diretamente no if pois não precisamnos salvar essa informação
if string_numero==string_numero[::-1]:
    print(string_numero," é igual de tras pra frente: ",string_numero[::-1])
else:
    print("não é")


