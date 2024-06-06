requests = [
    ["create", "xyz", "1", "1619916081"],
    ["join", "xyz", "2", "1619916681"],   
    ["create", "abc", "3", "1619916881"],
    ["leave", "xyz", "2", "1619920281"],
    ["join", "abc", "4", "1619920881"],
    ["create", "ghi", "5", "1619923999"],
    ["leave", "xyz", "1", "1619923881"],
    ["leave", "abc", "3", "1619927481"],
    ["leave", "abc", "4", "1619927481"],
    ["leave", "ghi", "5", "1619958001"]
]

# Find total time spent in each space over all users
#  {'xyz': 11400, 'abc': 17200, 'ghi': 34002}.)

dd={}

for req in requests:
    op=req[0]
    name=req[1]
    user=req[2]
    time=int(req[3])
    
    if op == "create":
        chat=[0,0,0]
        plist=[]
        plist.append((user, time))
        chat[0]=user
        chat[1]=plist[:]
        chat[2]=0
        dd[name]=chat
    elif op == "join":
        chat=dd[name]
        plist=chat[1][:]
        plist.append((user, time))
        chat[1]=plist[:]
        dd[name]=chat[:]
    elif op == "leave":
        chat=dd[name]
        plist=chat[1][:]
        dif_time=0
        for ip, p in enumerate(plist):
            if p[0] != user:
                continue
            time0=p[1]
            dif_time=time-time0
            del plist[ip]
            break
            
        chat[1]=plist[:]
        chat[2]+=dif_time
        dd[name]=chat[:]
        

print(dd)
