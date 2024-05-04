class test:
    def __init__(self) -> None:
        self.s1=[]
        pass

    def enq(self, x):
        s2=[]
        l1=len(self.s1)
        # copy to s2 in reverse order
        for i in range(l1):
            s2.append(self.s1.pop())
        self.s1.append(x)
        for i in range(l1):
            self.s1.append(s2.pop())
    def enq1(self, x):
        s2=[]
        l1=len(self.s1)
        if l1 ==0:
            self.s1.append(x)
        else:
            s2=self.s1[:]
            # print("..s2", s2)
            s1=[]
            self.s1.append(x)
            # print("..s1 after append",self.s1)
            s1=s1+s2
            # print("..s1 after sum",self.s1)

    def deq(self):
        x=self.s1.pop()
        return x


t=test()
q=int(input())
# print("q")
for i in range(1, q+1):
    line=input()

    ops=line.split(" ")
    # print("==ops", ops)
    type=ops[0]
    if type == "1":
        x=ops[1]
        t.enq1( x)
    if type == "2":
        x=t.deq()
    if type == "3":
        print(t.s1[len(t.s1)-1])
    # print("after op s1", t.s1)
