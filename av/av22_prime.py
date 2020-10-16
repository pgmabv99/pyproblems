import math
class t:

    def __init__(self,maxp):
        self.plist=[]
        self.nlist=[]
        self.maxp=maxp
        for i in range(maxp):
            self.plist.append(1)
            self.nlist.append(i+1)

    def scan(self):
        ipos=1    #start with number 2
        lp=len(self.plist)
        sqrt1=math.sqrt(self.maxp)
        print(sqrt1)
        while ipos <=  math.sqrt(self.maxp):
            inum=ipos+1
            j=inum
            print("inum j",inum, j)
            while True:
                if j+inum >lp:
                    break
                self.plist[j-1+inum]=0     #next 
                j=j+inum
            print(self.plist)
            ipos=ipos+1
       
        print(self.nlist)
        





t1=t(20)
t1.scan()
