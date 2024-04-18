from typing import List
# Write any import statements here
from collections import deque
def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
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