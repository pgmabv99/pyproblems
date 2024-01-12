
class node:
    def __init__(self, id):
        self.id=id
        self.l=None
        self.r=None


class tree:
    def __init__(self):
        n0=node(0)
        n0.l=node(1)
        n0.r=node(2)
        n0.l.l=node(3)
        n0.l.r=node(4)
        n0.r.r=node(6)
        self.root=n0

        n0=node(0)
        n0.l=node(1)
        n0.r=node(2)
        n0.l.l=node(3)
        n0.l.r=node(4)
        n0.r.l=node(6)
        self.root1=n0

    def walk_prt(self, n, level, side):
        if n:
            sp="="*level*2
            print(sp,n.id, side)
            self.walk_prt(n.l, level+1,"l")
            self.walk_prt(n.r, level+1,"r")

    def walk_swap(self, n):
        if n:
            self.walk_swap(n.l )
            self.walk_swap(n.r)
            zz=n.l
            n.l=n.r
            n.r=zz

    def node_cmp(self,n, n1):
        if (n and n1 ):
            print("match", n.id, n1.id)
            return True
        elif  (not n and not n1):
            print("match 2 Nones")
            return True
        else :
            print(f"mimsmatch ", n.id if n else None, n1.id if n1 else None)
            return False

    def walk_cmp(self, n, n1):

        if not self.node_cmp(n, n1):
            return False
        if n:
            print("go left")
            if not self.walk_cmp(n.l, n1.l):
                return False
            print("go right")
            if not self.walk_cmp(n.r, n1.r):
                return False
            return True
        else:
            return True




t=tree()

# t.walk_prt(t.root, 0, "root")
# t.walk_swap(t.root)
# t.walk_prt(t.root, 0)

t.walk_prt(t.root, 0, "root")
t.walk_prt(t.root1, 0, "root")
t.cmp=t.walk_cmp(t.root, t.root1)