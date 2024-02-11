

from typing import List
# Write any import statements here
v_list=[]
amt_list=[]

def step_profit(V,S, i, j):
    prof=0
    for k in range(i+1,j):
        prof+=V[k]*(1-S)
    prof+=V[j]
    return prof

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  # Write your code here
    print("V", V)
    i=0
    j=0
    t_amt=0

    while j < N:
        #decide on J
        prof=step_profit(V,S,i,j)
        if prof>= C:
            amt_list.append(prof)
            #enter
            v_list.append(j)
            i=j
            t_amt+=prof
        j+=1

    print("selected",end= " ")
    for x in v_list:
        print(V[x], "," , end="")
    print("\n")
    print("amt list" , *amt_list)



    return t_amt

# getMaxExpectedProfit(5, [10, 2, 8, 6, 4], 3, 0.5 )
getMaxExpectedProfit(5, [10, 2, 8, 6, 4], 3, 0.15 )
