
p=[10,9,10,11,8,12, 13, 2]
# p=[ 2,3]
# p=[3, 2,3]
m=len(p)
i=0
d1=None
d2=None
dl=[]
while i<=m-2:
    print("next",i, "p" ,p[i])
    if p[i+1] > p[i]:
        d1=i

        j=i+1
        while j < m-1 :
            if p[j+1]<p[j]:
                break
            j+=1
        d2=j
        print("d1 d2",d1,d2)
        d=(d1,d2)
        dl.append(d)
        i=j
    else:
        i+=1

print("final d1 d2",d1,d2)
print(dl)

max2=0
tot=0
for d in dl:
    d1,d2=d
    prof=p[d2]-p[d1]
    print(d1, d2, "prof", prof)
    max2=max(max2, prof)
    tot+=prof
print ("max tot", max2, tot)
