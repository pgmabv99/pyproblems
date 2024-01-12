
class node:
    def __init__(self, id) -> None:
        self.id=id
        self.next=None
        pass

class tree:


    def __init__(self) -> None:
        n0=node(0)
        self.root=n0
        n1=node(1)
        n0.next=n1
        n2=node(2)
        n1.next=n2
        pass

    def prt(self):
        print("== root", self.root)
        n=self.root
        while n :
            print (n.id)
            n=n.next
            
    def remkey(self,key):
        n=self.root
        prev=0
        while n:
            if n.id == key:
                n_tmp=n
                if prev:
                    prev.next = n.next
                    n=prev
                else:
                    self.root=n.next
                    n=self.root
                del n_tmp
            prev=n
            if n:
                n=n.next



t=tree()
t.remkey(2)
t.prt()
t.remkey(1)
t.prt()
t.remkey(0)
t.prt()
