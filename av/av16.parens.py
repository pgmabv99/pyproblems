
x1=["(", "(",")","(",")"]

class t:

    st=[]

    def check(self,p):
        i=0
        lenp=len(p)
        is_good=True
        while i < lenp:
            if p[i]=="(":
                t.st.append(p[i])
            elif p[i]==")":
                if len (t.st)==0 :
                    print("err: unbalanced: left paren  missing")
                    is_good=False
                    break
                else:
                    t.st.pop()
            else:
                print("err:bad input")
                continue
            i=i+1
        #any left parens left ?
        if len(t.st)>0:
            print("err: unbalanced: right  paren  missing")
            is_good=False
        return is_good


t1 =t()
res=t1.check(x1)
print ("string is_good", x1 , res)

