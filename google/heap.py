import heapq
ar= [4, 3, 17, 1, 8, 15, 18, 19,20]



def walk(ar,i,lev):
    if lev == 0:
        print(ar)
    spc="=="*lev
    if i > len(ar) -1:
        return
    print(spc,ar[i])
    walk(ar,2*i+1,lev+1)
    walk(ar,2*i+2,lev+1)


def mypush(ar,x):
    ar.append(x)
    i=len(ar)-1
    while i>0 :
        pi=i//2
        if ar[pi] > ar[i]:
            #swap
            z=ar[pi]
            ar[pi]=ar[i]
            ar[i]=z
        else:
            break
        i=pi

# walk(ar,0,0)

heapq.heapify(ar)
walk(ar,0,0)
ar1=ar[:]
ar2=ar[:]

heapq.heappush(ar1,5)
walk(ar1,0,0)


mypush(ar2, 5)
walk(ar2,0,0)
