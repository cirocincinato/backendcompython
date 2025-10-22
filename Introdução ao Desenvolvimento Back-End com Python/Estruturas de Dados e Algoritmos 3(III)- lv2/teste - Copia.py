n=int(input())
tabuada=[n*i for i in range(1,11)]
i=1
for valor in tabuada:
    print(f"{i}x{n}={valor}")
    i+=1


'''
n=int(input())
for i in range(0,n):
    x=int(input())
    if x==0:
        print("NULL")
    elif x%2==0:
        if x>0:
            print("EVEN POSITIVE")
        if x<0:
            print("EVEN NEGATIVE")
    else:
        if x<0:
            print("ODD NEGATIVE")
        if x>0:
            print("ODD POSITIVE")

x=[1,4,5,-4,-3,3]
ids=[id_x for id_x in range(len(x))]
page=1
limit=3
start=(page-1)*limit
end=start+limit
ordenado=sorted(x)

listaOrdena=[
    {x:i}
    for x in ids
    for i in ordenado[start:end]
    
]
print(listaOrdena)


'''

















