
slst="abcde"
pdc={
    "a":"ef"
    ,"c":"mn"
    ,"e": "a"
    }
wrk=[]
for i,s in enumerate(slst):
    if s in pdc:
        plst=pdc[s]
        for p in plst:
            #check order
            tail=slst[min(i+1,len(slst)):]
            if p in tail:
                print("loop", s, p)
                exit()

            if p not in wrk:
                wrk.append(p)
    if s not in wrk:
        wrk.append(s)
print(wrk)
