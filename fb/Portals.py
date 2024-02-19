from typing import List
import copy
# Write any import statements here


def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    t=test(R,C,G)
    t.find_start()
    # print("start", t.i0, t.j0)
    t.bldPort()
    t.step(t.i0,t.j0)
    # t.stack()

    # print("endList" , t.endList)
    # for _,_,_,path in t.endList:
    #     print("path", path.keys())
    # print(G)
    print ("ret", t.minsec)
    return t.minsec

class test:
    def __init__(self, R, C, G) -> None:
        self.i0=None
        self.j0=None
        self.R=R
        self.C=C
        self.G=G
        self.path={}
        self.endList=[]
        self.portMap={}
        self.minsec=-1
        self.sec=0

        pass

    def bldPort(self):
        for i in range(self.R):
            for j in range(self.C):
                c=self.G[i][j]
                if c not in("S","E","#", "."):
                    xlist=None
                    if c in self.portMap:
                        xlist=self.portMap[c]
                    else:
                        xlist=[]
                    xlist.append((i,j))
                    self.portMap[c]=xlist
        # print("portMap", self.portMap.items())


    def find_start(self):
        found=False
        for i in range(self.R):
            for j in range(self.C):
                if self.G[i][j]=="S":
                    found=True
                    self.i0=i
                    self.j0=j
                    break
            if found : break
        return

    def step(self,i,j):
        # print("step into", i, j)
        chr= self.G[i][j]
        if chr=="E":
            # print("end ", i, j, "sec", self.sec)
            self.endList.append((i,j,self.sec))
            if self.minsec == -1:
                self.minsec= self.sec
            else:
                self.minsec=min(self.minsec, self.sec)
            return
        if chr =="#":
            # print("wall ", i, j)
            return
        if (i,j) in self.path:
            # print(" in path")
            return


        self.path[(i,j)]=1
        self.sec+=1

        if i>0 :
            self.step(i-1,j)
        if i<self.R-1:
            self.step(i+1,j)
        if j>0 :
            self.step(i,j-1)
        if j<self.C-1:
            self.step(i,j+1)

        if chr in self.portMap:
            xlist=self.portMap[chr]
            for xi,xj in xlist:
                if (xi,xj) not in self.path and self.G[xi][j]!="#":
                    self.step(xi,xj)
            pass

        self.path.pop((i,j))
        self.sec-=1
        return

    def append22(self,stk, i, j):

        stk.append((i,j,copy.deepcopy(self.path),self.sec))
        return

    def pop22(self,stk):
        i,j, tmp, self.sec=stk.pop()
        self.path=copy.deepcopy(tmp)
        return i, j

    def prt_stk(self,stk):
        print("==== stack")
        if len(stk):
            for _,j,path,_ in stk:
                print("j",j)
                print("path", end=" ")
                for _,jx in path.keys():
                    print(jx,end=" ")
                print(end="\n")
        else:
            print("empty")
        return

    def stack(self ):

        stk=[]
        self.append22(stk,self.i0,self.j0)
        while len(stk)> 0:
            # self.prt_stk(stk)
            i,j =self.pop22(stk)
            # print("step into",  j)
            chr22= self.G[i][j]
            if chr22=="E":
                # print("end i j ", i , j)
                self.endList.append((i,j,self.sec,copy.deepcopy(self.path)))
                if self.minsec == -1:
                    self.minsec= self.sec
                else:
                    self.minsec=min(self.minsec, self.sec)

                continue
            if chr22 =="#":
                # print("wall ", i, j)
                continue
            if (i,j) in self.path:
                # print(" in path")
                continue


            self.path[(i,j)]=1
            self.sec+=1

            if i>0 :
                self.append22(stk,i-1,j)
            if i<self.R-1:
                self.append22(stk,i+1,j)
            if j>0 :
                self.append22(stk,i,j-1)
            if j<self.C-1:
                self.append22(stk,i,j+1)

            if chr22 in self.portMap:
                xlist=self.portMap[chr22]
                for xi,xj in xlist:
                    if (xi,xj) not in self.path and self.G[xi][j]!="#":
                        self.append22(stk,xi,xj)

        return


G1=[ [".","E","."]
   ,[".","#","E"]
   ,[".","S","#"]]

getSecondsRequired(3,3,G1)

G2=[ ["a",".","S","a"]
   ,["#","#","#","#"]
   ,["E","b",".","b"]]

getSecondsRequired(3,4,G2)

G3=[ ["a","S",".","b"]
   ,["#","#","#","#"]
   ,["E","b",".","a"]]

getSecondsRequired(3,4,G3)

G4=[ ["x","S",".",".","x",".",".","E","x"]
  ]

getSecondsRequired(1,9,G4)

# G5=[ ["x","S","E","x"]
#   ]

# getSecondsRequired(1,4,G5)
