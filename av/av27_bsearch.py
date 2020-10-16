import math
class test_t:

    def find_m(self,s_list, l, h):
        print("enter find_m", l, h)
        m=None
        m1=math.floor((l+h)/2)
        while m1<=h :
            if len(s_list[m1])>0:
                m=m1
                break
            m1=m1+1
        if m==None:
            while m1>=l :
                if len(s_list[m1])>0:
                    m=m1
                    break
                m1=m1-1 
        print("middle", m)
        return m

    def find(self,s_list, l, h, s):
        print("enter find", l, h)
        found=None
        if l>h:
    
            return found
        m=self.find_m(s_list,l,h)
        if m==None :
            return found
        if s==s_list[m]:
            #found
            found=m
            return found
        elif s>s_list[m]:
            m=self.find(s_list, m+1, h, s)
            found=m
        else :
            m=self.find(s_list, l, m-1, s)
            found=m

        return found
    # def find(self,s_list, l, h, s):
    #     found=None
    #     if l>=h-1 :
    #         if s==s_list[l]:
    #             found=l
    #         elif s==s_list[h-1]:
    #             found=h
    #         return found
    #     m=self.find_m(s_list,l,h)
    #     if s==s_list[m]:
    #         #found
    #         found=m
    #         return found
    #     elif s>s_list[m]:
    #         m=self.find(s_list, m, h, s)
    #         found=m
    #     else :
    #         m=self.find(s_list, l, m, s)
    #         found=m

    #     return found



s_list=["aa","","bb","","cc"]
t1=test_t()
str="bb"
str="a "
found=t1.find(s_list,0,len(s_list),str)
print(s_list,str,found)