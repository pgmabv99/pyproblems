# tree trunc compute


class node:
    def __init__(self, v) -> None:
        self.v=v
        self.chld=[]
        self.rp=[]
        self.rpres=[]
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
        root.rpres=inter_rp(root.rpres,node.rp)
        print("trunc")
        print_rp(root.rpres)

    for c in node.chld:
        walk(c, node, root)





walk(root, None, root)
