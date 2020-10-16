
# Say you have an array, A, for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.

# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


class t:
    

    def find(self):
        t.act_list=[]
        for i in range(t.len-1):
            if A[i+1] >A[i] :
                t.act_list.append(1)
            elif A[i+1] < A[i]:
                t.act_list.append(-1)
            else:
                t.act_list.append(0)
        #last day
        t.act_list.append(-1)


    def act(self):
        i=0
        while i<t.len:
            print("begin of double cycle",i)
            buy_day=None
            #find buy_day
            while i<t.len:
                    
                if t.act_list[i]==1:
                    print("buy",i,A[i])
                    t.B-=A[i]
                    break
                i=i+1  

            #find sell_day
            while i<t.len:
                if t.act_list[i]==-1:
                    print("sell",i,A[i])
                    t.B+=A[i]
                    break
                i=i+1  

A=[1, 2, 3]

t.len=len(A)
t.B=0
root=t()
root.find()
print(A)
print(t.act_list)
root.act()

print ("final bal", t.B)