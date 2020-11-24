# find smallest positive number that is NOT present in the array


def Solution(a):
    x=sorted(a)
    i=0
    lx=len(x)
    v=None
    for i in   range(lx):
      if i>0:
          if(x[i]-x[i-1]>1):
              v=x[i-1]+1
    
    if v==None :
        v=x[lx-1]+1
    if v<0 :
        v=1
    return v
    


A=[1,2,3, 0, 5]
print(A,Solution(A))
A=[1,2,3,4, 5]
print(A,Solution(A))
A=[-2,-23]
print(A,Solution(A))