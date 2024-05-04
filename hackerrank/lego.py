def legoBlocks(n, m):
    stk=[]
    global ngood,debug
    ngood=0

    def good():
        global debug
        dc={}  # mp number to how many breaks with this offset
        for b in stk:
            i=b[0]
            rm=i%m
            if rm == 0:
                # skip left of the wall
                continue
            if rm not in dc:
                dc[rm]=1
            else:
                dc[rm]+=1
        # print(dc)
        fl =True
        for rm in dc:
            if dc[rm] >= n:
                fl=False
                if debug :
                    print("crack at ",rm, dc)
        return fl


    def show():
        i=0
        for b in stk:
            w=b[2]
            s=str(w)*w
            print(s,end="")
            i+=w
            if i == m:
                print("")
                i=0
        print("==")
        return

    def add_brick(i,j,w):
        stk.append((i,j,w))
        next(i+w,j)
        stk.pop()

    def next(i, j):
        global ngood,debug
        if i == m and j == n-1:
            # reached bottom rigth
            fl=good()
            if fl:
                ngood+=1
            else:
                if debug:
                    show()
        elif i == m and j< n-1:
            # reached end of row. start next row
            next(0,j+1)
        else:
            for w in range(1,4):
                if( i+w <= m):
                    add_brick(i,j,w)
        return

    # main line
    debug =True
    debug =False
    # start at top left
    next(0,0)

    return ngood

# print(legoBlocks(2,3))
print("number of good walls without crack: ",legoBlocks(4,4))