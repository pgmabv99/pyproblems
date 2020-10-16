import math

# aab

# xxxxy
# x x xxy 
# xx xx y


class pat_t:

    def comp(self, s, istr, lcomp,ncomp):
     
        if istr+lcomp>len(s):
            return False


        s1=s[istr:istr+lcomp]
        print("consumed", s1)
        
        if ncomp==1 :
            return True
        istr=istr+lcomp
        icomp=1
        while icomp<=ncomp-1:
            if icomp+lcomp>len(s):
                return False
            s2=s[istr:istr+lcomp]
            print("consumed",s2)
            if s2!=s1:
                return False
            icomp=icomp+1
            istr=istr+lcomp
        
        return True


    def find(self, s, p, istr, ip,sect):
        if istr==len(s) and ip==len(p):
            print("matchd", s , "to", p, "sect", sect)
            return
        if istr==len(s) or ip==len(p):
            print("leaf reached  ", istr,ip)
            return 

        n=p[ip]
        max_lcomp=math.floor((len(s)-istr)/n)
        for lcomp in range(1,max_lcomp+1):
            match=self.comp(s,istr,lcomp,n)
            sect.append(s[istr:istr+lcomp]*n)
            if match :
                self.find(s,p,istr+lcomp*n,ip+1,sect)
                sect.pop()
        return 
        


t=pat_t()
# t.find("aaaab",[2,1],0,0,[])
t.find("aaaa",[2,1],0,0,[])
# t.find("aab",[2,1],0,0,[])