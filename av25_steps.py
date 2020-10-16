

class stk_t:
    def __init__(self):
        self.junk=""

class game_t:


    def run(self,lim):

        stk=stk_t()
        stk.step=0
        stk.dist=0
        stk.path=[0]

        stk_list=[]
        stk_list.append(stk)
        npath=0
        npop=0
        while len(stk_list)>0:

            stk=stk_list.pop()
            npop=npop+1
            dist=stk.dist+stk.step
            path=stk.path
            if dist >=lim:
                #reached end/leaf
                npath=npath+1
                print("==path completed", dist, lim, path) 

                continue
            else :
                #push all options
                for i in range(1,4):
                    if dist+i>lim:
                        continue
                    stk=stk_t()
                    stk.dist=dist
                    stk.step=i
                    #copy path
                    path1=path.copy()
                    path1.append(i)
                    stk.path=path1

                    stk_list.append(stk)
            

        print("total num paths" , npath, "pops" ,npop)

    def run_r(self,lim,step,stk1,dict):
        stk=stk1.copy()
        stk.append(step)
        if lim in dict:
            n=dict[lim]
            return n
        if(lim>=3):
            n=self.run_r(lim-1,1,stk,dict)+self.run_r(lim-2,2,stk,dict)+self.run_r(lim-3,3,stk,dict)
        elif lim==2:
            stka=stk.copy()
            stka.append(2)
            print(2, stka)
            stka=stk.copy()
            stka.append(1)
            stka.append(1)
            print(2, stka)
            n=2
        elif lim==1:
            stka=stk.copy()
            stka.append(1)
            print(1, stka)
            n=1
        elif lim==0:
            print(0, stk)
            n=1
        else:
            print("bad", lim)
        dict[lim]=n
        return n

game=game_t()
lim=5
game.run(lim)
npath=game.run_r(lim,0,[],{})
print("npath recursive",npath)



