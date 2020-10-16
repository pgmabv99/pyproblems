# Problem Description

# A message containing letters from A-Z is being encoded to numbers using the following mapping:

#  'A' -> 1
#  'B' -> 2
#  ...
#  'Z' -> 26
# Given an encoded message A containing digits, determine the total number of ways to decode it modulo 109 + 7.

A=[1,2,3,3]
A=[2,3, 1,3, 2]

class t:

    def __init__(self,parp,nump):
 
        self.par=parp
        self.children=[]
        self.num=nump
        if parp!=None:
            parp.children.append(self)

    def print_leaf(self):
        if len(self.children)==0:
            node=self
            num_list=[]
            while node!=None:
                num_list.append(node.num)
                node=node.par
            print("leaf",num_list)
        for child in self.children:
            child.print_leaf()


    def cnt(self,par,i):
        print("enter at pos" ,i)
        if (i==t.len-1):
            twin1=t(self,A[i])
            print("leaf  " ,i)
            return 1
        if (i==t.len):
            print("post leaf pos " ,i)
            return 1

        #cnt1 from 1 dig
        #new branch 

        twin1=t(self,A[i])
        cnt1=twin1.cnt(self,i+1)

        #cnt2 from 2 dig
        cnt2=0
        if i<= t.len-2:
            if 10*A[i]+A[i+1]<=26:
                twin2=t(self,10*A[i]+A[i+1])
                cnt2=twin2.cnt(self,i+2)

        cnt=cnt1+cnt2
        return cnt

#     
root=t(None,0)
t.len=len(A)
count=root.cnt(None,0)
print("final", count)

root.print_leaf()
