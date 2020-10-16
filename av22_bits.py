


#000100111000
#000101110000

class t:

    def tstbit(self,n,i):
        z=1<<i
        z=n & z
        if z==0:
            return 0
        else:
            return 1

    def setbit(self,n,i):
        z=1<<i
        res =n | z
        return res

    def clrbit(self,n,i):
        z=1<<i
        z=~z
        res =n & z
        return res




    def find_len(self, n):
        nbit=0
        for i in range(0,32):
            if self.tstbit(n,i)==1:
                nbit=nbit+1
        return nbit

    def find_large(self,nbit):
        hbit=31
        res=0
        for i in range(nbit):
            res=res+2**(hbit-i)
        return res

    def find_small(self,n):
        i=0
        
        ib1=None
        while i<32:
            if self.tstbit(n,i)==1:
                ib1=i
                break
            i=i+1
      
        ib2=None
        while i<32:
            if self.tstbit(n,i)==0:
                ib2=i
                break
            i=i+1

        res=n
        res=self.setbit(res,ib2)
        res=self.clrbit(res,ib1)
        return res



# t1=t()
# n=10
# print(bin(n))
# nbit=t1.find_len(n)
# res_h=t1.find_large(nbit)
# print(bin(res_h))

# res_l=t1.find_small(n)
# print(bin(res_l))




