
class stk_t:
    def __init__(self,node,dir,lev,par):

        self.node=node
        self.dir=dir
        self.lev=lev
        self.par=par


class node_t:
    hh=0

    def __init__(self, pv):
        self.v=pv
        self.children=[]
 

    def copy(self):
        node2=node_t("")
        node2.v=self.v+"_copy"
        return node2





class test_t:

        
    #pre-order with stack 
    def trav_nr_pre(self, root):
        print(" ")
        print("++++pre-order++++++")

        stk_list=[]

        dir=0
        lev=0
        node=root
        stk_p=stk_t(node,dir,lev,None)
        stk_list.append(stk_p)

        while len(stk_list)>0:
                 
            stk_p=stk_list.pop()
            node_p=stk_p.node
            lev=stk_p.lev
            par=stk_p.par
            print("popped from stack value", node_p.v, "lev", lev )
            node_p1=node_p.copy()
            if(par!=None):
                par.children.append(node_p1)
            else:
                root1=node_p1
            
     
            #push children and remember current as thier parent 
            for child in reversed(node_p.children):
                stk_p=stk_t(child,dir,lev+1,node_p1)
                stk_list.append(stk_p)

        #end loop
        return root1


    #post order with stack and copy
    def trav_nr_post(self,root):
        print(" ")
        print("++++post-order++++++")

        stk_list=[]

        dir="down"
        lev=0
        node=root
       
        stk_p=stk_t(node,dir,lev,None)

        stk_list.append(stk_p)
        
        while len(stk_list)>0:
            stk_p=stk_list.pop()

            node_p=stk_p.node
            dir=stk_p.dir
            lev=stk_p.lev

            # print("popped from stack value", node_p.v, "lev", lev, "dir ", dir)
            if (len(node_p.children)==0):
                print("Leaf lev" , lev, "value ",node_p.v  )
             
            else:
                if dir=="down":
                    #down 
                    #reappend(push) current  with dir=up 
                    stk_p=stk_t(node_p,"up",lev,None)
                    stk_list.append(stk_p)
                    for child_p in reversed(node_p.children):
                        stk_p=stk_t(child_p,"down",lev+1,None)
                        stk_list.append(stk_p)
                else:
                    #print and skip
                    print("up   lev" , lev, "value ",node_p.v )
                    
        #end loop
        return 



    



root=node_t("a")
c1=node_t("c1")
c2=node_t("c2")
c3=node_t("c3")
root.children.append(c1)
root.children.append(c2)
root.children.append(c3)

g11=node_t("g11")
g12=node_t("g12")
c1.children.append(g11)
c1.children.append(g12)
g21=node_t("g21")
c2.children.append(g21)
gg211=node_t("g211")
g21.children.append(gg211)


test_p=test_t()

root1=test_p.trav_nr_pre(root)
root2=test_p.trav_nr_pre(root1)



test_p.trav_nr_post(root2)



