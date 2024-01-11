

def test( s, lst):
    # lst.sort()
    if lst.min() > s:
        return False
    if lst.max()*2 <s:
        return False
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i]+lst[j] == s:
                print (i, j)
                return True
    return False

def test2( s, lst):
    set2= set()

    for n in lst:
        if s-n in set2:
            return True
        set2.add(n)
    return False

print(test2(9,[3,7,2]))