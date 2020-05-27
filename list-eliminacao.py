def josephus_survivor(l,k):
    lista=[]
    for i in range(1,l+1):
        lista.append(i)
    k1=k-1
    while len(lista)>1:
        if len(lista)<=k1:
            k1=k1%len(lista)
            n=lista[k1]
            lista.remove(n)
        else:
            lista.remove(lista[k1])
        k1+=k-1
    return lista[0]
