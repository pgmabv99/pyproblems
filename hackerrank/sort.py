
class srt:
    def __init__(self) -> None:
        pass

    def sort_merge(self,a):
        lx=len(a)
        if lx <= 1:
            print("term",a)
            return(a)

        mid=(lx+1)//2
        x=a[:mid]
        y=a[mid:]
        print(mid,x,y)
        sx=self.sort_merge(x)
        sy=self.sort_merge(y)

        res2=self.merge(sx,sy)
        return(res2)

    def merge(self,x,y):
        res=[]
        ix=0
        iy=0
        lx=len(x)
        ly=len(y)
        while ix<lx and iy<ly:
            if x[ix]<=y[iy]:
                res.append(x[ix])
                ix+=1
            else:
                res.append(y[iy])
                iy+=1
        if len(x[ix:]) >0:
            res+=x[ix:]
        if len(y[iy:]) >0:
            res+=y[iy:]
        return(res)

        pass

# a=[9,7,2,4,3,7,8]
# psrt=srt()
# print( psrt.sort_merge(a))
# print(psrt.merge([1,3,6],[2,4]))


class heap:
    EXTRA=3
    TMIN=1
    TMAX=2

    def __init__(self,type) -> None:
        self.hp=[]
        self.type=type
        pass

    def good_comp(self,x,y):
        res=False
        if self.type==heap.TMIN:
            if self.hp[x]<=self.hp[y]:
                res = True
        if self.type == heap.TMAX:
            if self.hp[x]>=self.hp[y]:
                res = True
        return res



    def flip_up(self, cur):
        print(" flip up", cur, self.hp[cur])
        while True:
            if cur <= 0:
                break
            par=(cur-1)//2
            # print("cur {} par {}".format(cur,par))
            if self.good_comp(par,cur):
                break
            self.hp[par],self.hp[cur]=self.hp[cur],self.hp[par]
            cur=par
        return

    def flip_down(self, cur):
        lc=2*cur+1
        rc=lc+1
        if lc < len(self.hp) and self.good_comp(lc,cur):
            self.hp[cur],self.hp[lc] = self.hp[lc],self.hp[cur]
            self.flip_down(lc)
        if rc < len(self.hp) and self.good_comp(rc,cur) :
            self.hp[cur],self.hp[rc] = self.hp[rc],self.hp[cur]
            self.flip_down(rc)
        return


    def add(self,x):
        # print("add ", x)
        self.hp.append(x)
        lh=len(self.hp)
        cur=lh-1
        self.flip_up(cur)

    def add_lst(self, arr):
        for x in arr:
            self.add(x)
        return


    def heapify(self, arr):
        self.hp=arr[:]
        lh=len(self.hp)
        last_non_leaf=lh//2-1

        for cur in range(last_non_leaf,-1,-1):
            self.flip_down(cur)
        return

    def pop(self):
        if len(self.hp) == 0:
            return None
        root_val=self.hp[0]
        x=self.hp.pop()
        self.hp[0]=x

        self.flip_down(0)
        return root_val

        return

    def print(self):
        off=heap.EXTRA
        par=0
        print("==========")
        tmp=[]
        for cur, x in enumerate(self.hp):
            x2=str(x)
            if cur*2+ 1 >= len(self.hp):
                x2+=":leaf"
            tmp.append(x2)
        print(tmp)


        self.print2(par,off)

    def print2(self,cur, off):
        # print("cur", cur)
        if cur >= len(self.hp):
            return

        space="-"*off
        print(space,  self.hp[cur])
        # print(space, cur, self.hp[cur])

        lc=2*cur+1
        rc=lc+1
        self.print2(lc, off+heap.EXTRA)
        self.print2(rc, off+heap.EXTRA)

class node:
    def __init__(self, k,v) -> None:
        self.k=k
        self.v=v
        self.lc=None
        self.rc=None
        self.par=None

        pass
class btree:
    LEFT=0
    RIGHT=1
    def __init__(self) -> None:
        self.root=None
        pass



    def sample(self):
        self.root=node(10,10)
        self.root.lc=node(6,6)
        self.root.rc=node(14,14)
        self.root.lc.lc=node(4,4)
        self.root.lc.rc=node(8,8)
        self.root.rc.lc=node(12,12)
        self.build_par(None, self.root)

    def build_par(self,par,cur):
        if cur == None:
            pass
        else:
            cur.par=par
            self.build_par(cur,cur.lc)
            self.build_par(cur,cur.rc)
        return

    def delete_node(self,cur):
        # adjust pointers from parent
        par=cur.par
        if par ==None:
            self.root=None
        elif par.lc == cur:
            par.lc = None
        else:
            par.rc = None

        # del  cur
        return

    def tprint(self):
        cur=self.root
        lev=0
        print("===tree")
        self.tprint2(cur, lev,"X")

    def tprint2(self,cur,lev,side):
        if cur == None:
            return
        parv=None
        if cur.par != None:
            parv=cur.par.v
        print("-"*lev,side,cur.v)
        # print("-"*lev,cur.v, "parv",parv)
        self.tprint2(cur.lc,lev+3,"L")
        self.tprint2(cur.rc,lev+3,"R")


    def search_key(self,cur,k):
        if cur == None:
            res=None
        elif cur.k==k:
            res=cur
        elif cur.k >k:
            res=self.search_key(cur.lc,k)
        else:
            res=self.search_key(cur.rc,k)

        return res

    def delete_key(self,k):
        rc=0
        cur=self.search_key(self.root,k)
        if cur ==None:
            rc = 1
        else:
            if cur.lc != None:
                max_ltr=self.find_max(cur.lc)
                # copy from it to cur
                cur.k=max_ltr.k
                cur.v=max_ltr.v
                self.delete_node(max_ltr)
            elif cur.rc != None:
                min_rtr=self.find_min(cur.rc)
                cur.k=min_rtr.k
                cur.v=min_rtr.v
                self.delete_node(min_rtr)
            else:
                self.delete_node(cur)

            pass
        return rc

    def insert_key(self,k):
        v=k
        cur=node(k,v)
        if self.root==None:
            self.root=cur
            cur.par=self.root
        else:
            gap=self.find_gap(self.root,None,k)
            if k <= gap.k:
                gap.lc=cur
            else:
                gap.rc=cur
            pass

        return


    def find_max(self, cur):
        if cur.rc !=None:
            res=self.find_max(cur.rc)
        else:
            res = cur
        return res

    def find_min(self, cur):
        if cur.lc !=None:
            res=self.find_min(cur.lc)
        else:
            res = cur
        return res

    def find_gap(self,cur,par,k):
        if cur ==None:
            res= par
        else:
            res=None
            if k<=cur.k:
                res= self.find_gap(cur.lc, cur, k)
            if res == None:
                res= self.find_gap(cur.rc, cur, k)


        return res



class heap_test:
    def __init__(self) -> None:
        pass
    def run(self):
        # pheap=heap(heap.TMIN)
        pheap=heap(heap.TMAX)

        arr=[2,1,4,-5,-4 , 6, 7,9, 25,-7]
        # arr=[2,1,4,-5]
        # pheap.add_lst(arr)
        # pheap.print()

        # top=pheap.pop()
        # print(top)
        # pheap.print()

        # pheap.add(top)
        # pheap.print()

        pheap.heapify(arr)
        pheap.print()
        return


class btree_test:
    def __init__(self) -> None:

        pass

    def run(self):
        pbtree=btree()
        pbtree.sample()
        pbtree.tprint()
        # search
        klist=[99,6,12]
        for k in klist:
            cur=pbtree.search_key(pbtree.root,k)
            res_v=None
            if cur != None:
                res_v=cur.v
            print("search for ", k, "res_v" , res_v)

        #  find min/max  in subtree
        k_list=[10, 6,4,14]
        for k  in k_list:
            cur=pbtree.search_key(pbtree.root,k)
            res_max=pbtree.find_max(cur)
            res_min=pbtree.find_min(cur)
            print("for cur", cur.v, "min",  res_min.v, "max " , res_max.v)

        # delete leaf  node
        # k_list=[4]
        # for k  in k_list:
        #     cur=pbtree.search_key(pbtree.root,k)
        #     pbtree.delete_node(cur)
        #     pbtree.tprint()

        # delete key
        # k_list=[14,10,6,8,12,4]
        # print("================test delete by keys",k_list)
        # pbtree.tprint()
        # for k  in k_list:
        #     pbtree.sample()
        #     print("delete key", k)
        #     pbtree.delete_key(k)
        #     pbtree.tprint()

        # k_list=[7,3,11,13]
        # for k in k_list:
        #     gap=pbtree.find_gap(pbtree.root, None,k)
        #     print("gap found",k,gap.k)

        k_list=[7,3,11,13,20, 18,21,22,23, 19]
        pbtree=btree()
        print("================test insert by keys",k_list)
        for k in k_list:
            gap=pbtree.insert_key( k)
            pbtree.tprint()

        pass

# pheap_test=heap_test()
# pheap_test.run()

pbtree_test=btree_test()
pbtree_test.run()