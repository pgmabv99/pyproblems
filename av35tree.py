# tree trunc compute


class node:
    def __init__(self, v) -> None:
        self.v=v
        self.chld=[]
        self.rp=[]
        self.trunk=[]
        pass


root=node("a")
root.chld.append(node("b"))
root.chld.append(node("c"))
root.chld[0].chld.append(node("d"))
root.chld[0].chld[0].chld.append(node("d1"))
root.chld[0].chld.append(node("e"))
root.chld[1].chld.append(node("f"))

def print_rp(rp):
    vlist=[]
    for node in rp:
        vlist.append(node.v)
    print(vlist)

def inter_rp(rp1, rp2) -> list:
    if len(rp1) == 0:
        return rp2
    res=[]
    i=0
    while i<len(rp1) and i<len(rp2) and rp1[i] == rp2[i] :
        res.append(rp1[i])
        i+=1
    return res

def walk(node, par, root):
    if len(node.chld)==0:
        leaf=True
    else :
        leaf=False

    print("enter ", node.v)
    # add current to rp
    if par != None:
        node.rp=par.rp[:]
    node.rp.append(node)
    if leaf :
        print("parent rp")
        print_rp(par.rp)
        print("node rp")
        print_rp(node.rp)
        root.trunk=inter_rp(root.trunk,node.rp)
        print("trunk")
        print_rp(root.trunk)

    for c in node.chld:
        walk(c, node, root)


def walk_stk(root):
    stk=[]
    rstk=[]
    stk.append(root)
    while len(stk)>0:
        cur=stk.pop()
        rstk.append(cur)
        print(f" current  from main stack  { cur.v} rp {cur.rp}")


        ich=0
        for ch in cur.chld:
            ch.rp=cur.rp[:]
            ch.rp.append(cur.v)
            stk.append(ch)
            ich+=1
        if len(cur.chld)==0:
            #leaf node . intersect rp
            root.trunk=inter_rp(root.trunk,cur.rp)

    print("reverse" , [ n.v for n in reversed(rstk)])
    print("original" , [ n.v for n in rstk])
    # print("reverse" , [ n.v for n in rstk[::-1]])
    return


# walk(root, None, root)

walk_stk(root)
print(f" trunk {root.trunk}")
