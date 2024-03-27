from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    # Write your code here
    t=test(N,L)
    t.loopBld11()
    # t.loopBld()
    # t.loopPrt()
    # t.loopBldMap()
    # t.loopPrtMap()
    print("ret maxl ", t.maxl)
    return t.maxl


class test:
    def __init__(self,N, L) -> None:
        self.N=N
        self.L=L
        pass



    def loopBld(self):
        self.loopCol=[]
        self.maxl=0
        for i  in range(1,self.N+1):
            if self.loopCheck(i):
                continue
            self.loopCol.append([])
            self.loopCol[-1].append(i)
            node=self.L[i-1]
            self.loopCol[-1].append(node)
            while True:
                node=self.L[node-1]
                if node in self.loopCol[-1]:
                    break
                self.loopCol[-1].append(node)
            self.maxl=max(len(self.loopCol[-1]),self.maxl)
            # self.loopPrt()
        pass

    def loopBld11(self):
        self.maxl=0
        self.visited=[0]*(self.N+1)
        for i  in range(1,self.N+1):
            if self.visited[i]==1:
                continue
            self.loop=[]
            self.loop.append(i)
            loopLen=1
            # self.visited[i]=1
            # node=self.L[i-1]
            # self.loop.append(node)
            # loopLen+=1
            # self.visited[node]=1
            node=i
            while True:
                node=self.L[node-1]
                if node in self.loop:
                    break
                self.loop.append(node)
                self.visited[node]=1
                loopLen+=1
            self.maxl=max(loopLen,self.maxl)
            print("i base1", i,  "loop", self.loop)
        pass

    def loopBldMap(self):
        self.loopCol={}
        self.maxl=0
        for i  in range(1,self.N+1):
            if self.loopCheckMap(i):
                continue
            self.loopCol[i]=set()
            self.loopCol[i].add(i)
            node=self.L[i-1]
            self.loopCol[i].add(node)
            while True:
                node=self.L[node-1]
                if node in self.loopCol[i]:
                    break
                self.loopCol[i].add(node)
            self.maxl=max(len(self.loopCol[i]),self.maxl)
            # self.loopPrtMap()
        pass

    def loopPrt(self):

        for i  in range(1,len(self.loopCol)+1):

            last =self.loopCol[i-1][-1]
            loopback =self.L[last-1]
            print("i base1", i,  "loop", self.loopCol[i-1], "last", last, "loopback", loopback)

            # for node in self.loopCol[i-1]:
            #     print( "index", node, "value", self.L[node-1])
        return

    def loopPrtMap(self):
        for i, loop in self.loopCol.items():

            print("i base1", i,  "loop", loop)
        return

    def loopCheck(self, i):
        for loop in self.loopCol:
            if i in loop:
                return True
        return False

    def loopCheckMap(self, i):
        for loop in self.loopCol.values():
            if i in loop:
                return True
        return False

getMaxVisitableWebpages(4, [4, 1, 2, 1])
getMaxVisitableWebpages(5, [4, 3, 5, 1, 2])
getMaxVisitableWebpages(5, [2, 4, 2, 2, 3])

# zeor index tests
# getMaxVisitableWebpages(4, [3, 0, 1, 0])
