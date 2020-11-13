class tree:

    def __init__(self):
        print("init")
        self.root=None

    def nav0(self):
        root=self.root
        root.nav1()
        


class node:

    def __init__(self, par, val):
        print("init node")
        self.val=val
        self.children=[]
        if par != None :
            par.children.append(self)

    def nav1(self):
        print(self.val)
        for child in self.children:
            child.nav1()



t1=tree()
n1=node(None,"av")
t1.root=n1
n2a=node(n1,"av2a")
n2b=node(n1,"av2b")
n3a=node(n2a,"av3a")

t1.nav0()