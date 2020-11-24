#one number in the other 

def solution(a ,b):
    # write your code in Python 3.6
    sa=str(a)
    sb=str(b)
    print(sa,sb)
    n=-1
    la=len(sa)
    lb=len(sb)
    if la > lb :
        return n
    for i in range (lb-la+1):
        print(sb[i:i+la])
        if(sa == sb[i:i+la]):
            n=i
            break
    return n

a=0
b=121100
print (a,b, solution(a,b))