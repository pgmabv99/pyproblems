
class tn:


    def __init__(self,data):
        self.data=data
        self.par=None
        self.twin=None
        self.ichild=0
        self.chs=[]
        self.self_done=False
        self.child_done=False

    def child_add(self,child):
        self.chs.append(child)
        child.par_add(self)

    def twin_add(self,twin):
        self.twin=twin

    def par_add(self,par):
        self.par=par
   
    
    def child_get(self):
        return self.chs
    
    #recursive
    def show(self):
        self.show_root_path()
        for ch in self.chs:
            if ch !=None:
                ch.show()

    #non recursive list of children pointer + parent pointer
    def show_nr_parent(self):
        p=self
        while p!=None:
            if p.self_done==False:
                #1st time path -process
                p.show_root_path()
                p.self_done=True
         
            if p.ichild<len(p.chs):
                if p.chs[p.ichild] !=None :
                    print("go down to ichild ", p.ichild)
                    pnext=p.chs[p.ichild]
                    # init children of 
                    pnext.ichild=0
                    p.ichild+=1
                    p=pnext
                    continue

            else:
                print("rigthmost child reached, go up")
                p=p.par   

    #non recursive twin pointer , 1st child pointer and parent 
    def show_nr_twin(self):
        p=self
        while p!=None:
            if p.self_done==False:
                #1st time path -process
                print(p.data)
                p.self_done=True
         
         
            if p.child_done==False:
                #attempt to go down
                if len(p.chs)>0 and  p.chs[0] !=None :
                    print("go down to child ")
                    pnext=p.chs[0]
                    p.child_done=True
                    p=pnext
                    continue
                else :
                    print("no children")
                    p.child_done=True


            if(p.twin!=None):
                print("go twin ")
                pnext=p.twin
                p=pnext
                continue
            else:
                print("go parent  ")
                pnext=p.par
                p=pnext
               

    def show_root_path(self):
        twin_data=None
        if self.twin !=None:
            twin_data=self.twin.data
        print(self.data, "::twin->" ,twin_data ,"         ::par_path",end = '' )
        parxx=self.par
        while parxx!=None:
            print("->", parxx.data, end = '' )
            parxx=parxx.par
        print()


r=tn("root")

c1=tn("c1")
r.child_add(c1)

c2=tn("c2")
r.child_add(c2)
c1.twin_add(c2)

g1=tn("g1")
c1.child_add(g1)



g21=tn("g21")
c2.child_add(g21)
g22=tn("g22")
g21.twin_add(g22)
c2.child_add(g22)

# r.show()
# r.show_nr_parent()
r.show_nr_twin()
