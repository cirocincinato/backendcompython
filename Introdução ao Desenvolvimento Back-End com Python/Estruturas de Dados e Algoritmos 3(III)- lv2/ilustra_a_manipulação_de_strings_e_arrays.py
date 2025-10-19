# Exemplo de manipulação de strings e arrays
def count_uppercase_segments(s):
    # Divide a string em segmentos que são armazenados em uma array lista

    segments = s.split()
    print("lista sem tratamento: ",segments)
    #apos usar a funçaõ .split() temos dentro da variavel segments=['Hello', 'World', 'This', 'Is', 'Python']
    #esse array agora pode ser ordenado
    # Conta quantos segmentos começam com letra maiúscula
    #count = sum(1 for segment in segments if segment[0].isupper())

    #mostrar cada palavra em ordem alfabetica na formatação expecifica 
    #ex: palavra0
    #    palvra1
    #    palvra2
    segments_ordenados=sorted(segments,key=lambda x:x[0])
    print("lista ordenada: ",segments_ordenados)

def calculate_running_sum(arr):
    # Calcula a soma acumulada de um array
    running_sum = []
    current_sum = 0
    for num in arr:
        current_sum += num
        running_sum.append(current_sum)
    return running_sum

# Testando as funções
string_example = "Hello World This Is Python"
array_example = [1, 2, 3, 4, 5]
count_uppercase_segments(string_example)
#print("Número de segmentos com maiúsculas:", count_uppercase_segments(string_example))
#print("Soma acumulada do array:", calculate_running_sum(array_example))
    