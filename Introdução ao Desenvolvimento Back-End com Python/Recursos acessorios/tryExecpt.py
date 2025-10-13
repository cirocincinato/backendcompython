try:
    numero=int("0")
    result=10/numero
except ValueError:
    print("erro: valor invalido")

except ZeroDivisionError:
    print("erro: não pode por zero")
