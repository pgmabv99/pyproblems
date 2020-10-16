
# Say you have an array, A, for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.

# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

#2 transactions B+s , B+s allowed

class t:
    

    def find(self):
        t.act_list=[]
        t.amt_list=[]
        for i in range(t.len-1):
            if A[i+1] >A[i] :
                t.act_list.append(1)
            elif A[i+1] < A[i]:
                t.act_list.append(-1)
            else:
                t.act_list.append(0)
            t.amt_list.append(A[i+1] - A[i])
            
        #last day
        t.act_list.append(-1)
        t.amt_list.append(-A[i+1])

    def find_max(self,k):
        t.amt_max_list=[]
        for i in range(k):
            mymax=0
            imax=None
            for j in range(t.len):
                if  t.amt_list[j]!=None and t.amt_list[j]>mymax:
                    mymax=t.amt_list[j]
                    imax=j
            #remember imax and exclude fro next iteration
            t.amt_list[imax]=None
            t.amt_max_list.append(imax)
        print(t.amt_max_list)



    def act(self):
        i=0
        while i<t.len:
            print("begin of double cycle",i)
            buy_day=None
            #find buy_day
            while i<t.len:
                    
                if i in t.amt_max_list:
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

A = [7, 2, 4, 8, 7]


t.len=len(A)
t.B=0
root=t()
root.find()
root.find_max(2)

print(A)
print("act_list",t.act_list)
print("amt_max_list",t.amt_max_list)
root.act()

print ("final bal", t.B)