a=[3,2,3]
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for chave,valor in dic.items():
    if valor>1:
        print("asda",chave)