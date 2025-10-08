# soma de 1 a N: receba um numero N e exiba a soma de todos os numeros de 1 até N.

#receber numero
N=int(input())

#vai rodar o a repetição ate N
#dentro do renge estou definindo de 1 ate N-1 
#ele ja esta soamndo previamente o valor que atribui a N então não preciso fazer o range com o valor de N+1
for i in range(1,N):

    #soma de todos os numeros de 1 até N
    #1+2+3+4+5+6...N
    N+=i
print(N)