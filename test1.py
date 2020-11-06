import math
def digitsManipulations(n):
    digs=[]
    while n>0 :
        n1=n%10
        digs.append(n1)
        n=math.floor(n/10)
    print(digs)

    mysum=0
    myprd=1
    for dig in digs:
        mysum +=dig
        myprd *=dig
    
    print(mysum, myprd)

    return myprd - mysum



print(digitsManipulations(12345)) 