
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


# Example usage:
# arr = [12, 11, 13, 5, 6, 7]
# arr = [3,2,1]
# heap_sort(arr)
# print("Sorted array:", arr)

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