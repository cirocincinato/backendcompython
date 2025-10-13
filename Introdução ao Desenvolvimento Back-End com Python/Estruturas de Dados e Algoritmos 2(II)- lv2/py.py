# Exemplo: Contar a frequência de caracteres em uma string
def contar_frequencia(s):
    frequencia = {}
    for char in s:
        if char in frequencia:
            frequencia[char] += 1
        else:
            frequencia[char] = 1
    return frequencia

# Teste da função
string_teste = "abracadabra"
resultado = contar_frequencia(string_teste)
print(resultado)

texto = "Python"
print(texto[0:5:3])