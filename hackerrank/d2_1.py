
def lonelyinteger(a):
    # Write your code here
    d={}
    for x in a:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    print(d)
    for k in d.keys():
        if d[k] == 1:
            print("key",k,"val",d[k])
            return d[k]

print(lonelyinteger([1,1,2]))