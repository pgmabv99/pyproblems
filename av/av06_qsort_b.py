
# x=[6,2]
x=[5,6,2,35,2, 7,7,81,1]
# x=[7,2,6,8]
# x=[2,2]

def swap(x,m, n):
    a=x[m]
    x[m]=x[n]
    x[n]=a

def pivot( x):
    xlen=len(x)
    pval=x[xlen-1]
    print("pval",pval)
    i=0
    j=0
    while j<= xlen-2:
        if x[j]<pval :
            swap(x,i,j)
            i=i+1
        j=j+1
    swap(x, i,xlen-1)
    return i

def quick_sort(x):
    print("enter sort ", x)
 
    if(len(x)<=1 ):
        print("bottom")
        return x

    pivot_p=pivot(x)
    pivot_v=[0]
    pivot_v[0]=x[pivot_p]
    print("after pivot position",pivot_p, x)

    x=quick_sort(x[0:pivot_p]) + pivot_v+ quick_sort(x[pivot_p+1:len(x)])
    return x



print(x)

x=quick_sort(x)

print(x)


    
