import math
class test:

    def run(self, x, l, h):
        print(l,h)
        magic=None
        if l==h :
            if x[l]==l:
                magic=l
            return magic
        m=math.ceil((l+h)/2)
        print(m)
        if x[m]==m:
            print("found" ,m )
            magic=m
        elif x[m]<m:
            magic=self.run(x,m,h)
        else: 
            magic=self.run(x,l,m-1)
        return magic


test1=test()
x=[0,1,9]
x=[0,3,4,5]
# x=[9,1,9]
magic=test1.run(x,0,len(x)-1)
print(x, magic)
