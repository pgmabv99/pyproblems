import math
class merge_t:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def fdif(self ,ix,iy):
        return abs(self.x[ix]-self.y[iy])

    def run(self):
        xlen=len(x)
        ix=0
        ylen=len(y)
        iy=0
        dif=self.fdif(ix,iy)

        

        while ix<xlen and iy<ylen:
            print(ix,iy)
            dif=min(dif,self.fdif(ix,iy))
            if x[ix]<y[iy]:
                ix=ix+1
            else:
                iy=iy+1

        return dif

    
x=[10, 2,   41]
y=[10.1,   41]


m=merge_t(x,y)
dif=m.run()
print(dif)