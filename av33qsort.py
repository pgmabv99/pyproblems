
def swap(x, i,j):
    a=x[i]
    x[i]=x[j]
    x[j]=a

#pivot around last element and return its position
def pivot(x,l,h):
    print()
    
    pv=x[h]
    p=None
    # for i in range(l,h-1):
    #     for j in range(i,h-1):
    #         if x[j]<pv:
    #             swap(i,j)
    l1=[]
    l2=[]
    for i in range(l,h):
        if x[i]<=pv:
            l1.append(x[i])
        else:
            l2.append(x[i])

    i=l
    for v in l1:
        x[i]=v
        i+=1
    x[i]=pv
    p=i
    i+=1
    for v in l2:
        x[i]=v
        i+=1
    return p

#pivot around last element and return its position
def pivot2(x,l,h):
    print()
    
    pv=x[h]
    p=None
    i=0
    j=0
    while j<=h-1:
        if x[j]<=pv:
            swap(x,i,j)
            i=i+1
        j+=1
    swap(x,i,h)
    return i



def qsortx(x,l,h):
    if l>= h:
        return
    p=pivot2(x,l,h)
    qsortx(x,l,p-1)
    qsortx(x,p+1,h)


x=[3,2, 5, 4,7, -4,3]
qsortx(x,0,len(x)-1)
print(x)
