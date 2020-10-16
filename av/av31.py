class test_t:

    def test1(self,p):
        mymax=None
        for i in range(len(p)):
            for j in range(i, len(p)):
                print(p[i:j])
                t=p[i:j]
                if mymax==None:
                    mymax=sum(t)
                else :
                    mymax=max(mymax,sum(t))
        return mymax

    def test1(self,p):
        mymax=None
        for i in range(len(p)):
            mysum=0
            for j in range(i, len(p)):
                
                t=p[i:j]
                if mymax==None:
                    mymax=sum(t)
                else :
                    mymax=max(mymax,sum(t))
        return mymax
                

t=test_t()
print(t.test1([0,1,2,3,4]))