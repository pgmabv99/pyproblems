x=[1,2,2,5,7,9,0,0,0,0]
y=[2,4,4,10]

xlen=len(x)
ylen=len(y)

#non empty len
xlen2=xlen
while (x[xlen2-1]==0):
    xlen2-=1

ix=0
for iy in range(ylen):

    # find insertion point 
    while ix<xlen2:
        print(ix,iy)
        if x[ix]<y[iy]:
            ix=ix+1
            continue
        else:
            break
        ix=ix+1
    ix_point=ix 
    print("ix oint",ix_point)
    #shift
    sx=xlen2
    while sx >ix_point:
        x[sx]=x[sx-1]
        sx=sx-1
    #extend
    xlen2=xlen2+1
    #insert
    x[ix_point]=y[iy]

    print(x)
