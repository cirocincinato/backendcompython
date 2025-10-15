# Exemplo de manipulação de strings e arrays
def count_uppercase_segments(s):
    # Divide a string em segmentos

    segments = s.split()

    # Conta quantos segmentos começam com letra maiúscula
    count = sum(1 for segment in segments if segment[0].isupper())
    return count

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

print("Número de segmentos com maiúsculas:", count_uppercase_segments(string_example))
print("Soma acumulada do array:", calculate_running_sum(array_example))
    