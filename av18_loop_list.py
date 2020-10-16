#link loop


class tnode:

    def __init__(self,pv):
        self.v=pv
        self.next=None
    


class tlist:

    def __init__(self):
        self.first=None

    def scan(self):
        p1=self.first
        #p2 ahead amd moving faster
        p2=self.first
        p2=p2.next
        loop=False
        
        while True:

            #double step
            p2=p2.next
            if p2 == None:
                break
            if p2==p1:
                loop=True
                break
            p2=p2.next
            if p2==None:
                break
            if p2==p1:
                loop=True
                break

            #single step
            p1=p1.next
        if loop==True:
            print("loop detected at " , p2.v) 
        else:
            print("no loop " ) 





tl1=tlist()
tn1=tnode(1)
tl1.first=tn1

tn2=tnode(2)
tn1.next=tn2

tn3=tnode(3)
tn2.next=tn3

tn4=tnode(4)
tn3.next=tn4

tn4.next=tn2


tl1.scan()