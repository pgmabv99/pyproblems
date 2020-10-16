from enum import Enum 

class wrktype_s(Enum):
    W_EMP=1
    W_MGR=2
    W_DIR=3   

class wrk_s:
    def __init__(self,type,name):
        self.name=name
        self.type=type
        self.avail=True
        self.call_p=None



class callstate_s (Enum):
    C_PENDING=1
    C_PROGRESS=2
    C_DONE=3
    C_ESCALATE=88
    C_ESCALATE2=99

class call_s:

    def __init__(self, quest):
        self.quest=quest
        self.state=callstate_s.C_PENDING
        self.wrk=None


class org:
  

    def __init__(self,name):
        self.name=name
        self.wrk_list=[]
        self.call_list=[] 

    def wrk_add(self,type, name):
        w=wrk_s(type,name)
        self.wrk_list.append(w)

    def call_p_add(self,quest):
       call_p=call_s(quest)
       self.call_list.append(call_p)

    def find_by_type(self,type):
        wrk_found=None
        for wrk in self.wrk_list:
            if wrk.type == type and wrk.avail==True:
                wrk_found=wrk
                break
        return wrk_found

    def find_by_name(self,name):
        wrk_found=None
        for wrk in self.wrk_list:
            if wrk.name == name :
                wrk_found=wrk
                break
        return wrk_found


    def route(self,call_p):
        #post wrk obj to  c
        if call_p.state ==callstate_s.C_PENDING:
            #initial call_p
            wrk_found=self.find_by_type(wrktype_s.W_EMP)
            if wrk_found!=None:
                return wrk_found
         
            wrk_found=self.find_by_type(wrktype_s.W_MGR)
            if wrk_found!=None:
                return wrk_found

            wrk_found=self.find_by_type(wrktype_s.W_DIR)
            if wrk_found!=None:
                return wrk_found

        elif call_p.state ==callstate_s.C_ESCALATE: 

            wrk_found=self.find_by_type(wrktype_s.W_MGR)
            if wrk_found!=None:
                return wrk_found

            wrk_found=self.find_by_type(wrktype_s.W_DIR)
            if wrk_found!=None:
                return wrk_found
        else:
            wrk_found=self.find_by_type(wrktype_s.W_DIR)
            if wrk_found!=None:
                return wrk_found

    #scan the list and route
    def route_list(self):
        for call_p in self.call_list:
            if call_p.state==callstate_s.C_PENDING or \
               call_p.state==callstate_s.C_ESCALATE  or \
               call_p.state==callstate_s.C_ESCALATE2 :
                wrk_found=self.route(call_p)
                if wrk_found!=None:
                    call_p.wrk=wrk_found
                    call_p.state=callstate_s.C_PROGRESS
                    wrk_found.avail=False
                    wrk_found.call_p=call_p
    #print list
    def print_call_list(self):
        print("calls:")
        for call_p in self.call_list:
            if call_p.wrk !=None:
                name=call_p.wrk.name
            else:
                name=None
            print(call_p.quest,call_p.state,name)

    #print list
    def print_wrk_list(self):
        print("wrks:")
        for wrk_p in self.wrk_list:

            print(wrk_p.name,wrk_p.avail,wrk_p.type)

    def resolve(self,call_p):
        wrk=call_p.wrk
        wrk.call_p=None
        wrk.avail=True
        call_p.wrk=None
        call_p.state=callstate_s.C_DONE

    def escalate(self,call_p):
        #free the worker
        wrk=call_p.wrk
        if wrk.type==wrktype_s.W_EMP:
            call_p.state=callstate_s.C_ESCALATE
        else :
            call_p.state=callstate_s.C_ESCALATE2
        #todo escalation above dir   
        wrk.call_p=None
        wrk.avail=True
        #todo move histroy to call
        call_p.wrk=None


    def exec(self, line):
        cmd_ops=line.strip().split()
        print(cmd_ops)
        cmd=cmd_ops[0]
        oper=None
        if len(cmd_ops)>=2:
            oper=cmd_ops[1]

        if cmd=="add":
            o1.call_p_add(oper)
        elif cmd=="res":
            wrk_found=self.find_by_name(oper)
            if wrk_found==None:
                print("worker not found ", oper)
                return
            elif wrk_found.avail==True:
                print("worker not busy")
                return 
            else  :        
                self.resolve(wrk_found.call_p)

        elif cmd=="esc":
            wrk_found=self.find_by_name(oper)
            if wrk_found==None:
                print("worker not found ", oper)
                return
            elif wrk_found.avail==True:
                print("worker not busy")
                return
            else:
                self.escalate(wrk_found.call_p)
        elif cmd=="exit":
            exit()
        else:
            print(cmd)






    def run(self) :
        f=open("files/cmd.txt", "r")
        self.route_list()
        self.print_call_list()
        for line in f :

            self.exec(line)

            print("before route")
            self.print_call_list()
            self.print_wrk_list()

            self.route_list()

            print("after route")
            self.print_call_list()
            self.print_wrk_list()



class test_s:
    def unit1(self):

        o1=org("myorg")

        o1.wrk_add(wrktype_s.W_EMP,"av")
        o1.wrk_add(wrktype_s.W_EMP,"ev")
        o1.wrk_add(wrktype_s.W_EMP,"lv")

        o1.wrk_add(wrktype_s.W_MGR,"mg")
        o1.wrk_add(wrktype_s.W_DIR,"dr")

        o1.call_p_add("where is my cheese")
        o1.call_p_add("where is my phone bill")

        o1.run()


test_p=test_s()

import math

i=0
while i <=90:
    print(i, math.cos(math.radians(i)))
    i=i+10

