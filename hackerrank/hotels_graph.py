
class test:
    def __init__(self,arr) -> None:
        self.path=[]
        self.min_lpath=0
        self.arr=arr
        self.lmap={}  # map length to triangle of that length
        self.distmap={}  #map of pair to length (cache)




    def get_lpath(self,c, targ):
        self.path.append(c)
        if c == targ:
            lpath=len(self.path)-1
            if self.min_lpath ==0:
                self.min_lpath=lpath
            else:
                self.min_lpath=min(self.min_lpath, lpath)
        else:
            # try all edges out of C (L-->R)
            for edge in self.arr:
                if edge[0] != c:
                    # wrong start
                    continue
                if edge[1] in self.path:
                    # end in self.path already
                    continue
                self.get_lpath(edge[1],targ)
            # try all edges out of C (R-->L)
            for edge in self.arr:
                if edge[1] != c:
                    # wrong start
                    continue
                if edge[0] in self.path:
                    # end in self.path already
                    continue
                self.get_lpath(edge[0],targ)
        self.path.pop()
        return

    def get_lpath2(self,c,targ):
        pair=(c,targ)
        # take from cache
        if pair in self.distmap:
            return self.distmap[pair]
        # compute and store in cache
        self.path=[]
        self.min_lpath=0
        self.get_lpath( c,targ)
        print( "start/target" ,c,targ, "self.min_lpath", self.min_lpath)
        # store in cache
        self.distmap[pair]=self.min_lpath
        return self.min_lpath

    def triangle(self,i,j, k):
        # trng=("i {} j {} k {}".format(i,j,k))
        trng=("{} {} {}".format(i,j,k))
        # print(trng)
        l1=self.get_lpath2(i,j)
        l2=self.get_lpath2(i,k)
        l3=self.get_lpath2(j,k)
        if l1 == l2 and l2 == l3:
            # good triangle . add self.lmap
            if l1 in self.lmap:
                v=self.lmap[l1]
                v[0]+=1
                v.append(trng)
                self.lmap[l1]=v
            else:
                v=[1,trng]
                self.lmap[l1]=v

        pass

    def run(self ):
        l2=len(self.arr)
        nc=0
        for edge in self.arr:
            nc=max(nc, edge[0], edge[1])
        print("num of cities", nc)

        self.get_lpath2( 2, 5)
        # self.get_lpath2(arr, 1, 5)
        # self.get_lpath2(arr, 3, 7)
        # self.get_lpath2(arr, 3, 8)
        # self.get_lpath2(arr, 8, 9)

        for i in range(1,nc+1):
            for j in range (i+1, nc+1):
                for k in range(j+1,nc+1):
                    self.triangle(i, j,k)
        print("self.lmap", self.lmap)
        pass



arr=[[1,2],[2,5],[3,4],[4,5],[5,6],[7,6],[8,9]]
arr=[[1,2],[2,5],[3,4],[4,5],[5,6],[7,6]]
arr=[[1,2],[1,3],[1,4],[1,5]]

arr=[]
n=5
for i in range(n):
    edge=[i,i+1]
    arr.append(edge)
    edge=[i,i+2]
    arr.append(edge)
    edge=[i+1,i+2]
    arr.append(edge)

t1=test(arr)
t1.run()