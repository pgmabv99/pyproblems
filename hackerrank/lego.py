def legoBlocks(n, m):
    from collections import Counter
    stk=[]
    global ngood,debug,ntot
    ngood=0
    ntot=0
    dc2=Counter()

    def good():
        global debug
        dc={}  # map number to how many breaks with this offset
        for b in stk:
            i=b[0]
            rm=i%m
            rm=i
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

    def next(i, j):
        global ngood,debug,ntot
        if i == m and j == n-1:
            # reached bottom rigth
            ntot+=1
            # fl=good()
            fl=True

            for rm in dc2:
                if rm == 0:
                    continue
                if dc2[rm] >= n:
                    fl=False

            if fl:
                ngood+=1
                if debug:
                    # print("good-----")
                    # show()
                    pass

            else:
                if debug:
                    print("bad------",dc2)
                    show()
                    pass
        elif i == m and j< n-1:
            # reached end of row. start next row
            next(0,j+1)
        else:
            for w in range(1,5):
                if( i+w <= m):
                    dc2[i]+=1
                    stk.append((i,j,w))
                    next(i+w,j)
                    stk.pop()
                    dc2[i]-=1
        return

    # main line
    debug =True
    debug =False
    # start at top left
    next(0,0)
    # print("tot",ntot)
    return ngood
##
# print(legoBlocks(2,3))
# print("number of good walls without crack: ",legoBlocks(2,2))
# print("number of good walls without crack: ",legoBlocks(3,2))
# print("number of good walls without crack: ",legoBlocks(2,3))
# print("number of good walls without crack: ",legoBlocks(4,4))
print("number of good walls without crack: ",legoBlocks(4,5))
print("number of good walls without crack: ",legoBlocks(4,6))
print("number of good walls without crack: ",legoBlocks(4,7))