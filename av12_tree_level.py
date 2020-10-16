class t:
    hh=0

    def __init__(self, pv):
        self.v=pv
        self.children=[]
        self.ichild=0


    def get_h(self,lev):
        print(self.v)
        if lev>t.hh :
            t.hh=lev

        for child in self.children:
            child.get_h(lev+1)

    #print tree levels using  matrix for intermediate storage
    def trav(self,lev):
        print(self.v)
        if lev>=len(m) :
            #add new level
            m.append([])
        #append node to row
        m[lev].append(self.v)
        for child in self.children:
            child.trav(lev+1)

    #print tree levels using double loop over height 
    def trav2(self,lev,print_lev):
        if lev>print_lev :
            return
        elif  lev==print_lev :
            print(self.v)
        else:
            for child in self.children:
                child.trav2(lev+1,print_lev)


        
    #pre-order with stack 
    def trav_nr_pre(self):
        print(" ")
        print("++++pre-order++++++")
        s=[]
        sv=[]
        slev=[]

        s.append(self)
        sv.append(self.v)
        slev.append(0)
    
        
        while len(s)>0:
            print("stack v ", sv)                   
        
            next=s.pop()
            val=sv.pop()
            lev=slev.pop()



            print("popped from stack", next.v)
            print("next ===========lev " , lev, "value ",next.v  )
            #increment global level to hold children

            for child in reversed(next.children):
                s.append(child)
                sv.append(child.v)
                slev.append(lev+1)
        #end loop


    #post order with stack
    def trav_nr_post(self):
        print(" ")
        print("++++post-order++++++")
        s=[]
        sv=[]
        sdir=[]
        slev=[]

        s.append(self)
        sv.append(self.v)
        sdir.append("down")
        slev.append(0)
    
        
        while len(s)>0:

            print("stack v ", sv)                   
            print("stack direction ", sdir) 
            next=s.pop()
            val=sv.pop()
            dir=sdir.pop()
            lev=slev.pop()



            print("popped from stack", next.v, "dir", dir)
            if (len(next.children)==0):
                print("next ====Leaf=======lev " , lev, "value ",next.v  )
            else:
                if dir=="down":
                    #down 
                    #reappend next with dir=up 
                    s.append(next)
                    sv.append(next.v)
                    sdir.append("up")
                    slev.append(lev)  
                    for child in reversed(next.children):
                        s.append(child)
                        sv.append(child.v)
                        sdir.append("down")
                        slev.append(lev+1)  
                else:
                    #print and skip
                    print("next ====up======================lev" , lev, "value ",val )



        #end loop



    



root=t("a")
c1=t("c1")
c2=t("c2")
c3=t("c3")
root.children.append(c1)
root.children.append(c2)
root.children.append(c3)

g11=t("g11")
g12=t("g12")
c1.children.append(g11)
c1.children.append(g12)
g21=t("g21")
c2.children.append(g21)
gg211=t("g211")
g21.children.append(gg211)

# m=[]
# root.trav(0)
# print(m)

# root.get_h(0)
# print("height",t.hh)
# for i in range(t.hh):
#     root.trav2(0,i)


root.trav_nr_pre()

root.trav_nr_post()



