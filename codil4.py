# you can write to stdout for debugging purposes, e.g.
from extratypes import Tree  # library with types used in the task

#scan tree fid longes path with no dups
def is_unique(path):
    x={}
    for p in path:
        if p in x :
            return False
        else:
            x[p]=1
    return True
 

def solution(T):
    stk=[]
    stkpar=[]
    stk.append(T)
    pathr=[T.x]
    stkpar.append(pathr)
    mymax=1
    
    while len(stk)>0:
        n=stk.pop()
        path1=stkpar.pop()
        path2=path1.copy()
        print(n.x)
        
        
        if n.l != None :
           stk.append(n.l)
         
           path1.append(n.l.x)
           stkpar.append(path1)
           if is_unique(path1) and len(path1)>mymax:
               mymax=len(path1)
               
           
        if n.r != None :
           stk.append(n.r)
           path2.append(n.r.x)
           stkpar.append(path2)
           if is_unique(path2) and len(path2)>mymax:
               mymax=len(path2)       
           
         
    return mymax