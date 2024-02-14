from typing import List
# Write any import statements here


def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    t=test(R,C,G)
    t.find_start()
    # print("start", t.i0, t.j0)
    t.bldPort()
    t.step(t.i0,t.j0)
    # print("endList" , t.endList)

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
            self.endList.append((i,j))
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
                self.step(xi,xj)
            pass

        self.path.pop((i,j))
        self.sec-=1
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
