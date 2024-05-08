#graph scan for shortest distance
#recursion
def bfs(n,edges, start):
    # Write your code here
    print(n,edges,start)
    global path
    dist=[-1]*(n)
    path=[]

    def next(x,s):
        print("enter ", x)
        global path
        path.append(x)
        l2=len(path)-1
        if dist[x-1] == -1:
            dist[x-1]=l2
        else:
            dist[x-1]=min(dist[x-1], l2)

        for edge in edges:
            if edge[0] ==  x and edge[1] not in path:
                next(edge[1],s)
            if edge[1] ==  x and edge[0] not in path:
                next(edge[0],s)

        path.pop()
        return

    # start
    next(start,start)


    return dist

#  with stack of paths
def bfs_stk(n, edges,start):
    dist_list=[-1]*(n)
    path=[]
    stk=[]
    stk.append(start)
    stk_path=[]
    stk_path.append(path[:])# stack of path
    i=0
    while len(stk) != 0 :
        i+=1
        if i >10 :
            break
        x=stk.pop(0)
        print("enter ", x)
        # restore path
        tmp=stk_path.pop(0)
        path=tmp[:]
        print("enter ", x, "restored path ", path)

        dist=len(path)
        path.append(x)

        if dist_list[x-1] == -1:
            dist_list[x-1]=dist
        else:
            dist_list[x-1]=min(dist_list[x-1], dist)

        for edge in edges:
            y=None
            if edge[0] ==  x and edge[1] not in path:
                y=edge[1]
            if edge[1] ==  x and edge[0] not in path:
                y=edge[0]
            if y != None:
                stk_path.append(path[:])     # remember path at this pint
                stk.append(y)
        pass


    return dist_list
# --

# without stack of path. TODO
def bfs_stk2(n, edges,start):
    dist_list=[-1]*(n)
    path_list=[[]]*n
    stk=[]
    prev=0
    stk.append((start, prev))
    i=0
    while len(stk) != 0 :
        i+=1
        if i >10 :
            break
        x,prev=stk.pop(0)
        print("enter ", x, "prev", prev)


        if prev==0:
            dist_list[x-1] =1
        else:
            if dist_list[x-1] == -1:
                dist_list[x-1] = dist_list[prev-1] +1
            else:
                dist_list[x-1] = min(dist_list[prev-1] +1, dist_list[x-1] )


        for edge in edges:
            next=None
            if edge[0] ==  x :
                next=edge[1]
            if edge[1] ==  x :
                next=edge[0]
            # todo avoid loops ???
            # if edge[0] ==  x and edge[1] not in path:
            #     next=edge[1]
            # if edge[1] ==  x and edge[0] not in path:
            #     next=edge[0]
            if next != None:
                stk.append((next,x))
        pass


    return dist_list
# --
n=7
start=2
edges=[[1,2],[2,4],[1,3],[2,5], [5,7],[3,5]]
# dist_list=bfs(n,edges,start)
dist_list=bfs_stk2(n,edges,start)
for i,d in enumerate(dist_list):
    print((i+1,d),end="")
print("\n")