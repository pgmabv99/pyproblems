

class vrt_t:
    def __init__(self,val):
        self.val=val
    def __del__(self):
        print("deleting vertex",self.val)

class edg_t:

    def __init__(self,vrt1,vrt2):
        self.vrt1=vrt1
        self.vrt2=vrt2
    def __del__(self):
        print("deleting edge",self.vrt1)   

class grp_t:
    def __init__(self, name):
        self.name=name
        self.vrt_list=[]
        self.edg_list=[]
    def __del__(self):
        print("deleting", self.name)

    def vrt_add(self, vrt_p):
        self.vrt_list.append(vrtp)

    def edg_add(self, vrt_p1, vrt_p2):
        edg_p=edg_t(vrt_p1,vrt_p2)
        self.edg_list.append(edg_p)

    def vrt_scan(self,vrt_p,hit_list):
        
        stk_list=[]

        stk_list.append(vrt_p)
        hit_list.append(vrt_p)

        while len(stk_list)>0:
            vrt_p=stk_list.pop()
            print("vertex ", vrt_p.val)
            
            #put all connected nodes on stack
            for edg_p in self.edg_list:
                if edg_p.vrt1==None:
                    continue
                #to do : need index/1st pointer for speed
                if edg_p.vrt1!=vrt_p:
                    continue
                if  edg_p.vrt2 in hit_list:
                    continue
                stk_list.append(edg_p.vrt2)
                hit_list.append(edg_p.vrt2)
            


    def vrt_scan_all(self):
        hit_list=[]
        for vrt_p in self.vrt_list:
            if vrt_p in hit_list:
                continue
            self.vrt_scan(vrt_p, hit_list)


    def vrt_copy(self,vrt_p,vrt_c,hit_list,vrt_listc,edg_listc):
        
        stk_list=[]

        stk_list.append(vrt_p)
        hit_list.append(vrt_p)
        vrt_listc.append(vrt_c)
     

        while len(stk_list)>0:
            vrt_p=stk_list.pop()
            vrt_c=stk_listc.pop()

            print("vertex ", vrt_p.val)
            
            #put all connected nodes on stack
            for edg_p in self.edg_list:
                if edg_p.vrt1==None:
                    continue
                #to do : need index/1st pointer for speed
                if edg_p.vrt1!=vrt_p:
                    continue
                if  edg_p.vrt2 in hit_list:
                    #todo link  is not copied
                    continue
                #navigation
                stk_list.append(edg_p.vrt2)
                hit_list.append(edg_p.vrt2)
                
                #copy vrt
                vrt2_c=vrt_t(edg_p.vrt2.val+100)
                vrt_listc.append(vrt2_c)
                stk_listc.append(vrt2_c)

                #copy edge
                edg_c=edg_t(vrt_c,vrt2_c)
                edg_listc.append(edg_c)

    def grp_copy2(self):
        grpc=grp_t("copy of " +self.name)
        grpc.vrt_list=[]
        dict1={}
     
        for i  in range(len(self.vrt_list)):
            vrt_p=self.vrt_list[i]
            # copy and add to target
            vrt_c=vrt_t(vrt_p.val+100)
            grpc.vrt_list.append(vrt_c)
            #maps for faster searches
            dict1[vrt_p]=i

        print(dict1)
        grpc.edg_list=[]

        hit_list=[]
        for i  in range(len(self.vrt_list)):

            vrt_p=self.vrt_list[i]
            if vrt_p in hit_list: 
                continue        
            stk=[]
            stk.append(vrt_p)
            while len(stk)>0:

                vrt_p=stk.pop()
                hit_list.append(vrt_p)

                i1=dict1[vrt_p]
                vrt1_c=grpc.vrt_list[i1]
                
                #iterate and get subset of links .. time intensive ??
                for edg_p in self.edg_list:
                    if edg_p.vrt1!=vrt_p:
                        continue

                    i2=dict1[edg_p.vrt2]
                    vrt2_c=grpc.vrt_list[i2]

                    edg_c=edg_t(vrt1_c,vrt2_c)
                    grpc.edg_list.append(edg_c)
                    if edg_p.vrt2 in hit_list:
                        continue
                    stk.append(edg_p.vrt2)




        return grpc
   

    def edg_show(self):
        print("graph",self.name)
        for edg_p in self.edg_list:
            print("edge", edg_p.vrt1.val,edg_p.vrt2.val)

    def grp_copy(self):
        grpc=grp_t("copy of " +self.name)
        grpc.vrt_list=[]
        dict1={}
     
        for i  in range(len(self.vrt_list)):
            vrt_p=self.vrt_list[i]
            # copy and add to target
            vrt_c=vrt_t(vrt_p.val+100)
            grpc.vrt_list.append(vrt_c)
            #maps for faster searches
            dict1[vrt_p]=i

        print(dict1)
        grpc.edg_list=[]
        for edg_p in self.edg_list:
            # vrt1_i=self.vrt_list.index(edg_p.vrt1)
            vrt1_i=dict1[edg_p.vrt1]
            vrt1_c=grpc.vrt_list[vrt1_i]
            # vrt2_i=self.vrt_list.index(edg_p.vrt2)
            vrt2_i=dict1[edg_p.vrt2]
            vrt2_c=grpc.vrt_list[vrt2_i]
            edg_c=edg_t(vrt1_c,vrt2_c)
            grpc.edg_list.append(edg_c)
            
        return grpc

class test_t:

    def test1(self):
        grp_p=grp_t("test")

        for i in range(7):
            grp_p.vrt_list.append(vrt_t(i))
        
        vrt_list=grp_p.vrt_list

        grp_p.edg_list.append(edg_t(vrt_list[0],vrt_list[1]))
        grp_p.edg_list.append(edg_t(vrt_list[1],vrt_list[2]))
        grp_p.edg_list.append(edg_t(vrt_list[1],vrt_list[5]))
        grp_p.edg_list.append(edg_t(vrt_list[2],vrt_list[0]))
        grp_p.edg_list.append(edg_t(vrt_list[3],vrt_list[2]))
        grp_p.edg_list.append(edg_t(vrt_list[3],vrt_list[4]))

        grp_p.edg_show()
        grp_p.vrt_scan_all()

        # grh_c=grp_p.grp_copy()
        grh_c=grp_p.grp_copy2()
        grh_c.edg_show()
        grh_c.vrt_scan_all()

        # del(grp_p)
        print("last statement")
      
    

  



        
t=test_t()
t.test1()
            