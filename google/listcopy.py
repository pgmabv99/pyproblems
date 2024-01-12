
class node:
    def __init__(self,id):
        self.id=id
        self.next=0
        self.p=0
        pass

def prt(root):
    n=root
    while n:
        # print(n, n.next, n.p, "id", n.id)
        print( "id", n.id,  n.p.id if n.p else "empty")
        n=n.next



n0=node(0)
n1=node(1)
n2=node(2)

n0.next=n1
n1.next=n2
n2.next=0

n0.p=n2
n1.p=n0
n2.p=n2
root =n0


print("initial")
prt(root)

#copy
n=root
root2=0
prev2=0
while n:
    n2=node(n.id)
    if root2 ==0:
        root2 = n2
    if prev2 :
        prev2.next=n2

    prev2=n2
    n=n.next


print("copy")
prt(root2)

#rebuild second pointer

n=root
n2=root2
while n:
    # walk both in step
    nx=root
    n2x=root2
    while nx:
        if nx== n.p:
            n2.p=n2x
            break
        nx=nx.next
        n2x=n2x.next

    n=n.next
    n2=n2.next

print("after ajust ptr")
prt(root2)