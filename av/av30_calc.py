
class calc_t:

    def find(self, s, i, ops):
        for op  in ops:
            j=s[i:len(s)].index(op)
            if j!=None:
                return j
        return len(s)


    #run till empty or left parens
    def run_stack(self, stk, sto):
        # stk=stk1.copy()
        # sto=sto1.copy()
        # stk1=stk1.reverse()
        # sto1=sto1.reverse()
        # print("reverse stack", sto, stk)
        while len(sto)>0:
            print("run stack", sto, stk)
            
            op=sto.pop()
            if op=="(":
                print("pop left paren")
                break

            v1=stk.pop()
            v2=stk.pop()
            if op=="+":
                res=v1+v2
            elif op=="-":
                res=v2-v1
            elif op=="*":
                res=v1*v2
            elif op=="p":
                res=v2**v1
            else :
                    print("bad op")
            stk.append(res)
        print("end stack", sto, stk)

    def comp(self,s,lev):
        d={}
        d["+"]=1
        d["-"]=1
        d["*"]=2
        d["/"]=2
        d["p"]=3
        d["("]=0

        i=0
        stk=[]
        sto=[]
        for i in range(len(s)):
            print("next", s[i],"comp",sto,stk)
            if s[i]=="(":
                sto.append(s[i])
            elif s[i]==")":
                self.run_stack(stk,sto)
            elif s[i]  in d:
                op=s[i]
                if len(sto)==0:
                   sto.append(op)
                else :
                    top_op=sto[len(sto)-1]
                    if d[op]<d[top_op]:
                        #low prty OP next. run the stack
                        self.run_stack(stk,sto)
                    elif top_op=="-" :
                        #. run the stack to do 1st minus
                        self.run_stack(stk,sto)

                    sto.append(op)
            else :
                #operand
                stk.append(int(s[i]))
        self.run_stack(stk,sto)
        print("res", s, stk[0])

                    

                    
        






t=calc_t()
exp=[1]
exp=[1,"+",2,"*",5, "-", 4,"p",2,"-",100]
exp=[1,"-","(",1,"-",1,")"]
exp="5+(1-2)*(2+2)p2+5"
exp="2*2*2+1+1"
exp="1+1+2*2*2+1"
exp="1-1+1-1-1-1"
t.comp(exp,0)
