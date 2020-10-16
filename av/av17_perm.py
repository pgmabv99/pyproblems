#permutations

class t:
    super_s=[]
    super_sum=[]
    super_sumx=[]


    #build list of permutations of k elements long
    def perm1(self, x,k, maxk, xset):
        if k<maxk:
            for i in range(len(x)):
                xset.append(x[i])
                #create list copy and remove x[i]
                x1=x.copy()
                x1.pop(i)
                #recursive call
                self.perm1(x1,k+1,maxk,xset)
                xset.pop()
        else:
            #set of k is ready :save it or compute sum now
            xset1=xset.copy()
            t.super_s.append(xset1)
            t.super_sum.append(sum(xset1))
             
    #end of

    #build list of permutations of k elements long
    def perm2(self, x,k, maxk, xset,sumx):
        if k<maxk:
            for i in range(len(x)):
                if x[i]!=None:
                    v=x[i]

                    xset.append(v)
                    sumx=sumx+v

                    #create list copy and remove x[i]
                    s=x[i]
                    x[i]=None
                    #recursive call
                    self.perm2(x,k+1,maxk,xset,sumx)
                    x[i]=s

                    xset.pop()
                    sumx=sumx-v
                else:
                    continue
        else:
            #set of k is ready :save it or compute sum now
            xset1=xset.copy()
            t.super_s.append(xset1)
            t.super_sum.append(sum(xset1))
            t.super_sumx.append(sumx)
    #end of

    def perm_all(self,x):
        maxk=1
        while maxk<=len(x):
            setx=[]
            sumx=0
            # self.perm1(x,0,maxk,setx)
            self.perm2(x,0,maxk,setx,sumx)
            maxk=maxk+1

    def show(self,x):
        print("x",x)
        print("super_s")
        for i in range(len(t.super_s)):
            print(t.super_s[i],t.super_sum[i],t.super_sumx[i])



x=[1,2,3,4]
t1=t()
t1.perm_all(x)
t1.show(x)