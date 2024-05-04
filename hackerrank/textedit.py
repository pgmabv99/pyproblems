# Enter your code here. Read input from STDIN. Print output to STDO
class test:
    def __init__(self):
        self.s=[]
        # self.s=""
        self.stk=[]
        return

    def append(self, w):
        tmp=self.s[:]
        self.stk.append(tmp)
        self.s+=w
        return

    def delete(self, k):
        tmp=self.s[:]
        self.stk.append(tmp)
        l2=len(self.s)
        # print("delete..",l2)
        self.s=self.s[:l2-k]
        # print("after del", self.s)

    def print1(self, k):
        print(self.s[k-1])

    def undo(self):
        print(self.stk)
        tmp=self.stk.pop()
        self.s=tmp[:]


f1=open("hackerrank/d.txt","r")
import sys
sys.stdin=f1

t=test()
q=int(input())
for i in range(q):
    ops=input().split(" ")
    # print(ops, t.s)
    print(ops)
    print("befor", "".join(t.s))
    if ops[0] == "1":
        t.append(ops[1])
    if ops[0] == "2":
        t.delete(int(ops[1]))
    if ops[0] == "3":
        t.print1(int(ops[1]))
    if ops[0] == "4":
        t.undo()
    print("after","".join(t.s))
