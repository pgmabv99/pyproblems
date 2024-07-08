

class t:
    def __init__(self, s):
        self.s=s
        pass
        
    def scan(self, sx):
        lx=len(sx)
        if lx == 0:
            return
        tmp=self.ld[lx-1][:]
        if sx not in tmp:
            tmp.append(sx)
            self.ld[lx-1]=tmp[:]
        # self.ld[lx-1].append(sx)
        for ichr in range(lx):
            lp=sx[:ichr]
            rp=sx[ichr+1:]
            sx2=lp+rp
            self.scan(sx2)
            
        pass
        
    def print2(self):
        print(self.subsets)
    

    def subset_str_build(self,str2):
        self.subsets=[""]
        for chr in str2:
            newstrs=[]
            for subset in self.subsets:
                newstr=subset+chr
                newstrs.append(newstr)
            self.subsets+=newstrs
        # self.subsets.sort(key=lambda s: len(s), reverse=True)
        # self.subsets.sort(key=lambda s: str(len(s)).zfill(5)+s, reverse=True)
        # self.subsets.sort( reverse=True)
        return self.subsets

        



def commonChild(s1, s2):
    # Write your code here
    print("inp s1", s1)
    print("inp s2", s2)
    t1=t(s1)
    t1.subset_str_build(s1)
    t2=t(s2)
    t2.subset_str_build(s2)
    t1.print2()
    t2.print2()
    inter=list(set(t1.subsets)&set(t2.subsets))
    if len(inter) == 0:
        return 0
    else: 
        inter.sort(key=lambda x: len(x), reverse=True)
        print("inter", inter)
        return len(inter[0])
    

      


il=commonChild("harry","sally")
# il=commonChild("ary","aly")
print(il)
# il=commonChild("abc","bc")
# print(il)

# def commonChild(s1, s2):
#     # Write your code here
#     print("inp s1", s1)
#     print("inp s2", s2)
#     t1=t(s1)
#     t1.subset_str_build(s1)
#     t2=t(s2)
#     t2.subset_str_build(s2)
#     t1.print2()
#     t2.print2()
#     i1=0
#     i2=0
#     while True:
#         if i1 == len(t1.subsets) or i2 == len(t2.subsets):
#             break
#         sx1 =t1.subsets[i1]
#         sx2 = t2.subsets[i2]
#         l1=len(sx1)
#         l2=len(sx2)
#         if l1 > l2 :
#             i1+=1
#         elif l2 > l1:
#             i2+=1
#         elif sx1 == sx2 :
#             il=len(sx1)
#             print(i1, i2 ,sx1)
#             return il
#         elif sx1 > sx2:
#             i1+=1
#         elif sx1 < sx2:
#             i2+=1

#     return 0
      