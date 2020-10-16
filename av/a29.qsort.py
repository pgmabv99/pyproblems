class sort_t:

    def swap(self,x,i, k):
        z=x[i]
        x[i]=x[k]
        x[k]=z
    
    def pivot(self,x, l,h):


        piv=h-1
        
        k=l
        i=l
        while k< h:
            if(x[k] < x[piv]):
                #swap i and k

                self.swap(x,i,k)
                i=i+1

            k=k+1
        
        # print(x,x[i])

        self.swap(x,i,piv)
        return i


    def qsort(self,x,l,h):
        print(l,h)
        if l<h:
            piv=self.pivot(x,l,h)
            self.qsort(x,l,piv-1)
            self.qsort(x,piv+1,h)
x=[5,1,2,3, 6,88,2]
t=sort_t()
print(x)
t.qsort(x,0,len(x))
print(x)
