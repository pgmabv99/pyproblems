
class test:
    
    def sort_str(self,s1):
        # print("in",s1)
        s2=[]
        for c in s1:
            s2.append(c)
        s2.sort()
        s3=""
        for x in s2:
            s3=s3+x
        # print("out",s3)
        return s3

    def sort_ang(self,x):

        print(x)
        x.sort(key=self.sort_str)
        print(x)




    
    def sort_ang_dict1(self,x):
        dict={}
        for s in x:
            ss=t.sort_str(s)
            if ss not in dict:
                dict[ss]=[s]
            else:
                dict[ss].append(s) 

        for key in sorted(dict):
            for s in dict[key]:
                print(s)

    def getter(self,key):
        print("key",key)
        return self.dict[key]
    
    def sort_ang_dict2(self,x):
        self.dict={}
        for s in x:
            ss=t.sort_str(s)
            self.dict[s]=ss
        print(self.dict)

        # for elm in sorted(self.dict,key=self.getter):
        #     print(elm)
        for elm in sorted(self.dict,key=lambda k: self.dict[k]):
            print(elm)

x=["ba","acd","ab", "cad"]
t=test()
# t.sort_ang(x)
# t.sort_ang_dict1(x)
t.sort_ang_dict2(x)
