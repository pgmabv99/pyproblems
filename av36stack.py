class stack:
    def __init__(self) -> None:
        self.lst=[]
        pass

    def pop(self):
        x=self.lst[-1]
        self.lst.pop()
        return x
    def push(self,x):
        self.lst.append(x)
    def is_empty(self)->bool:
        if len(self.lst) == 0:
            return True
        else:
            return False


from typing import List
from collections import deque
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:

  tot_list=[]
  #add intial position
  C2=[1]+ C[:]
  # Write your code here
  def check(i, tot):
    print(f"check i {i} prev tot = {tot} ")
    if i==M:
      print("appen tot", tot)
      tot_list.append(tot)
      return
    print(f" new pair {C2[i]} {C2[i+1]}")

    # hg vsh los

    dif=C2[i+1]-C2[i]
    print("dif ", dif)
    if dif < 0 :
      dif=-dif
    #forward
    check(i+1, tot+dif)
    #back
    check(i+1, tot+N-dif)

    return





  check(0,0)
  tot_final=10**10
  for tot in tot_list:
    if tot < tot_final:
      tot_final=tot
  print("tot_list", tot_list)
  return tot_final

def getMin2(N: int, M: int, C: List[int]):
    tot_fin=10**10
    #add intial position
    C2=[1]+ C[:]
    sti=deque()
    stt=deque()
    sti.appendleft(0)
    stt.appendleft(0)

    while sti :
        i=sti.pop()
        tot=stt.pop()
        # print(f"popped i {i}  tot {tot}")

        if i==M:
            if tot < tot_fin:
                tot_fin=tot
            # print(f"reach leaf .added {tot_list}")
        else:
            # take next follwing 2 path
            dif=abs(C2[i+1]-C2[i])
            # print(f"dif {dif}")
            sti.appendleft(i+1)
            stt.appendleft(tot+dif)

            sti.appendleft(i+1)
            stt.appendleft(tot+N-dif)
        pass

    return tot_fin

def getMin22(N: int, M: int, C: List[int]):
    tot_fin=10**10
    #add intial position

    sti=deque()
    stt=deque()
    stp1=deque()
    stp2=deque()
    sti.appendleft(0)
    stt.appendleft(0)
    # stack init position
    stp1.appendleft(1)
    stp2.appendleft(1)
    while sti :
        i=sti.popleft()
        tot=stt.popleft()
        cp1=stp1.popleft()
        cp2=stp2.popleft()
        print(f"popped i {i}  tot {tot} cp1 {cp1} cp2 {cp2}")

        if i==M:
            if tot < tot_fin:
                tot_fin=tot
            print(f"reach leaf .added {tot_fin}")
        else:
            # take next follwing 2 path
            dif1=min(abs(C[i]-cp1),N-abs(C[i]-cp1))
            dif2=min(abs(C[i]-cp2),N-abs(C[i]-cp2))
            # print(f"dif {dif}")

            # try wheel1
            sti.appendleft(i+1)
            stt.appendleft(tot+dif1)
            stp1.appendleft(C[i])  #new previous
            stp2.appendleft(cp2)   #unchanged

             # try wheel2
            sti.appendleft(i+1)
            stt.appendleft(tot+dif2)
            stp1.appendleft(cp1)    #unchanged
            stp2.appendleft(C[i])   #new prev

        pass

    return tot_fin

def getMin3(N: int, M: int, C: List[int]):

    tot_fin=0
    cp =1
    #add intial position

    for c in C:
        dif=min(abs(c-cp),N-abs(c-cp))
        tot_fin+=dif
        cp=c


    return tot_fin

def getMin4(N: int, M: int, C: List[int]):

    tot_fin=0
    cp1 =1
    cp2 =1
    #add intial position

    for c in C:
        dif1=min(abs(c-cp1),N-abs(c-cp1))
        dif2=min(abs(c-cp2),N-abs(c-cp2))
        if dif1 < dif2:
            cp1=c
            tot_fin+=dif1
        else:
            cp2=c
            tot_fin+=dif2

    return tot_fin


# print("res", getMinCodeEntryTime(3,3,[1,2,3]))
# print("res", getMinCodeEntryTime(10,4,[9, 4, 4, 8]))
# print("res", getMin2(3,3,[1,2,3]))
# print("res", getMin2(10,4,[9, 4, 4, 8]))
# print("res", getMin3(3,3,[1,2,3]))
# print("res", getMin3(10,4,[9, 4, 4, 8]))
print("res", getMin22(3,3,[1,2,3]))
print("res", getMin22(10,4,[9, 4, 4, 8]))