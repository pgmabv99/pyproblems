import math

# find x*(x+1)==n

def t1(m):
    if m<=0:
        return 0
    else:
        l= math.floor(math.sqrt(m))-1
        h=math.ceil(math.sqrt(m))

    # print("mlh",m, l, h)
    i=l
    while i<=h:
   
        # print("i",i)
        if i*(i+1)==m:
             return 1
        i=i+1
    return 0





def solution(a ,b):
    

    mcount=0
    n=a
    while n<=b:
        if (n/2 -math.floor(n/2))==0 :
            mcount=mcount+t1(n)   
        n=n+1

    return mcount

a=6
b=20
print ("sol",a,b, solution(a,b))
a=21
b=29
print ("sol",a,b, solution(a,b))
a=1
b=2
print ("sol",a,b, solution(a,b))