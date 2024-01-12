
bl=[["s","g"],["x","x"],["s","x"]]

objs=["s","g"]

def f1(bl, objs):
    dist_x_glb=[]
    for i in range(len(bl)):
        dist={}
        for obj in objs:
            dist[obj] = 999

        for j in range(len((bl))):
            for obj in objs:
                if obj in bl[j]:
                    if abs(j-i) < dist[obj]:
                        dist[obj]=abs(j-i)
        print(dist)

        dist_x=max(dist.values())
        dist_x_glb.append(dist_x)



    print(dist_x_glb)
    print(dist_x_glb.index(min(dist_x_glb)))

def f2(bl, objs):
    dist_max_list=[]
    for i in range(len(bl)):
        #build dict of nearest objects
        dist={}

        for obj in objs:
            #search outward
            dist[obj]=999
            for j in range(i,len(bl),1):
                if obj in bl[j] and j-i < dist[obj]:
                    dist[obj]=j-i
                    break
            for j in range(i-1,-1,-1):
                if obj in bl[j] and i-j < dist[obj]:
                    dist[obj]=i-j
                    break

        print(dist)
        dist_max=max(dist.values())
        dist_max_list.append(dist_max)

    print(dist_max_list)

# f1(bl,objs)
f2(bl,objs)
