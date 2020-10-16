import math
class test_t:

    def nzero(self,n):

        lg=math.floor(math.log10(n))
        print(lg)
        t=0
        for i in range (1,lg):
            nz=math.floor(n/(10**i))
            t=t+nz

            print(nz)

test_p=test_t()
test_p.nzero(1185)
