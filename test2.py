def bmatch(s,p,i):
    lp=len(p)
    match=0
    for j in range(lp):
        if p[j]=="0" and s[i+j] in ['a', 'e', 'i', 'o', 'u',  'y'] :
            match+=1
        elif  p[j]=="1" and s[i+j] not in ['a', 'e', 'i', 'o', 'u',  'y'] :
            match+=1
    if match==lp :
        return 1
    else:
        return 0

def binaryPatternMatching(pattern, s):
    p=pattern
    ls=len(s)
    lp=len(p)
    cnt=0
    for i in range (ls-lp+1) :
        found=bmatch(s,p,i)
        cnt +=found
    
    return cnt
        
print(binaryPatternMatching ("010","amazing"))
