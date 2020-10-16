
# compute pathes in matrix 0,0 -> m.n 
#avoid obstacles in A
class Solution:

    def check_i(self,i,j):
        res=True
        if i==Solution.maxi:
            res=False
        else:
            next=[i+1,j]
            print("next in ", next , Solution.obs )
            if next in Solution.obs:
                res=False
        return res
    def check_j(self,i,j):
        res=True
        if j==Solution.maxj:
            res=False
        else:
            next=[i,j+1]
            if next in Solution.obs:
                res=False
        return res


    def step(self, i,j):
        if i==Solution.maxi and j==Solution.maxj :
            return 1
        ni=0
        nj=0
        if(self.check_i(i,j)==True):
             ni=self.step(i+1,j)
        if(self.check_j(i,j)==True):
            nj=self.step(i,j+1)
        print (i, j, "ni, nj" , ni, nj)
        return ni+nj
    
    def uniquePathsWithObstacles(self, A):
        Solution.obs=A
        Solution.maxi=2
        Solution.maxj=2
        if [0,0] in Solution.obs:
            npath=0
        else:
            npath=self.step(0,0)
        return npath


    
x=Solution()
A=[
  [1, 0,]

]

npath=x.uniquePathsWithObstacles(A)
print(npath)