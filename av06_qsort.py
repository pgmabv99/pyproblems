
# x=[6,2]
x=[5,6,2,35,2, 7,7,81,1]
x=[7,2,6,5]
# x=[2,2]

def swap(m, n):
    a=x[m]
    x[m]=x[n]
    x[n]=a

def pivot( low,high):
   
    pval=x[high]
    print("pval",pval)
    i=0
    j=0
    while j<= high:
        if x[j]<pval :
            swap(i,j)
            i=i+1
        j=j+1
    swap(i,high)
    return i

def quick_sort(low,high):
    print("enter ", low, high, x[low:high+1])
 
    if(low >=high ):
        print("bottom")
        return
    pivot_p=pivot(low,high)
    print("after pivot ",pivot_p, x)
  
    quick_sort( low, pivot_p-1)
    quick_sort(pivot_p+1,high)


print(x)

quick_sort(0,len(x)-1)

print(x)


    
