
xlist=[10, 8, 4, 5, 9]
xlist=[10, 20, 11, 21]
xlist=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

# -build tree of XLIST  where child node value >= parent 
# -attach such children to each parent where above True
# -for the ready tree find the biggest depth

# t=tree_init()

# for x in xlist
#   tree_attach(t,x)

# ml=tree_scan(t) for longest


class t:
    max_lev=0
    def __init__(self, vp):
        self.v=vp
        self.children=[]
        self.level=0
        self.par=None

    def t_add_child(self,vp):
        child=t(vp)
        self.children.append(child)
        child.level=self.level+1
        child.par=self
        print("added", child.v , "under ", self.v)

    def leaf_scan(self,vp):

        #iterate over children
        for child in self.children:
            child.leaf_scan(vp)

        if self.v ==None :
                self.t_add_child(vp)
        else : 
            if self.v <= vp:
                self.t_add_child(vp)
            
    #scan to find max
    def leaf_scan_max(self):
        if len(self.children)==0:
            print("leaf lev", self.level, "val",self.v) 
            if self.level>t.max_lev:
                t.max_lev=self.level
            
        else :
            #iterate over children
            for child in self.children:
               child.leaf_scan_max()
               
    #scan to print  max
    def leaf_scan_max_print(self):
        if len(self.children)==0 and self.level==t.max_lev:
            root_p=[self.v]
            parx=self.par
            while parx !=None:
                root_p.append(parx.v)
                parx=parx.par
            root_p.reverse()
            print(root_p)
            
        else :
            #iterate over children
            for child in self.children:
               child.leaf_scan_max_print()


root=t(None)
root.level=1
xlen=len(xlist)
for i in range(xlen):
    root.leaf_scan(xlist[i])

t.max_lev=0
root.leaf_scan_max()
print("max",t.max_lev -1)

root.leaf_scan_max_print()
 

