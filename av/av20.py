class seq:
    #repesent continious sequence of 1s
    def __init__(self,ps):
        self.s=ps
        self.l=None

class t:
    #list onumbers 0/1 correspnding to bits
    t.xlist=[]
    #list of sect object
    t.sec_list=[]

    def tesbit(self,n,i):
        mask=1<<i 
        res=n&mask
        if res !!= 0 :
            return 1
        else:
            return 0

    def bit_2_list(self,num):
        #todo +1 

        lg=ceil(math.log2(num))+1
        for nbit in range(lg):
            res=tesbit(num,nbit)
            t.xlist.append[res]
     

    def bldseq(self):

        i=0
        xlen=len(t.xlist)
        while i<xlen
            if x[i]==0 :
                i=i+1
                continue
            #start section on "1"
            xsec=sec(i)
            #look for end
            j=i
            while j<xlen
                if(x[j])==0:
                    break
                j=j+1
            #either found "0" or end
            xsec.l=j-i
            #added to list
            t.xsec_list.append(xsec)
            i=j

        print(len(t.xsec_list))

    def seq_friends(self):
        for i in range(len(t.xsec_list)-1):
            s=t.xsec_list[i].s
            l=t.xsec_list[i].l
            if s+l+1==s=t.xsec_list[i+1].s:
                t.xsec_list[i].l2=t.xsec_list[i].l+1+t.xsec_list[i+1].l

    def find_max(self):

        xmax=0
        imax=0
        for i in range len(t.xsec_list) :
            if t.xsec_list[i].l >xmax:
                xmax=t.xsec_list[i].l
                imax=i

        xmax2=0
        imax2=0
        for i in range len(t.xsec_list) :
            if t.xsec_list[i].l2 >xmax2:
                xmax2=t.xsec_list[i].l2
                imax2=i

        if imax>=imax2:
            res_bit=t.xsec_list[imax].s +t.xsec_list[imax].l
        else:
            #add with friend.. boundary may be diff
            res_bit=t.xsec_list[imax].s +t.xsec_list[imax].l
        return res_bit



    





num=222
t1=t()
t1.bit_2_list(num)
t1.bldseq()
t1.seq_friends()
res=t1.find_max()
print (res)
