def next_bigger(n):
    a=[]
    b=[]
    for i in str(n):
        a.append(int(i))
        b.append(int(i))
    b=sorted(a)
    b.reverse()
    if max(a)==min(a) or b==a:
        return -1
    else:
        v=False
        l=len(a)-1
        k=len(a)-1
        c=-1
        w=[]
        while v==False:
            if k<0:
                c-=1
                l-=1
                k=len(a)-1+c
                continue
            w.append(a[k])
            for i in w:
                if a[k]<i:
                    a.insert(k,i)
                    a.pop(len(a)-1-w.index(i))
                    a[k+1:]=sorted(a[k+1:])
                    v=True
                    break
                elif(a[l]>a[k]):
                    a.insert(k,a[l])
                    a.pop(l+1)
                    a[k+1:]=sorted(a[k+1:])
                    v=True
                    break
            k-=1
        return int(''.join([str(i) for i in a]))
