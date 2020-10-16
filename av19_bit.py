

Move bits from on enum to anotherimport math

class bit:

    def setbit(self,num,i):
        print ("in setbit", num ,bin(num),i)
        x=1<<i
        num2=num | x
        
        print("out",num2,bin(num2))
        return num2

    def offbit(self,num,i):
        print ("in offbit",num, bin(num),i)
        x=1<<i
        x=~x
        num2=num & x
        print("out",num2,bin(num2))
        return num2

    def tesbit(self,num,i):
        print ("in tesbit",num, bin(num),i)
        x=1<<i
        y=num & x
        if(y>0):
           print("ret on")
           return 1
        else:
           print("ret off")
           return 0

    def insert(self,m,n,i,j):
        print("n m ", n, bin(n), m, bin(m), "i j",i,j)
        lg=math.ceil(math.log2(m))
        for k in range(i-j+1):
        # for k in range(lg):
            b=self.tesbit(m,k)
            if b==1:
                n=self.setbit(n,j+k)
            if b==0:
                n=self.offbit(n,j+k)
        print("n ", n, bin(n))





b=bit()
# num=8
# num2=b.setbit(num,0)
# num3=b.setbit(num2,1)
# b.tesbit(num2,0)
# b.tesbit(num2,1)
# num3=b.offbit(num2,0)

n=2**10
m=19
i=6
j=2
b.insert(m,n,i,j)


