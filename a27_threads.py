import threading
import time
import random

class msg_t:

    def  __init__(self, test_p):
        self.buf=["aaaa"]
        self.empty=threading.Semaphore()
        self.full=threading.Semaphore()
        self.avail=threading.Condition()
        test_p.myprint("acquire  both empty and full  at start")
        self.empty.acquire()
        self.full.acquire()


 

class test_t:

    def __init__(self):
        self.prt=threading.Condition()

    def myprint(self, *args):
        self.prt.acquire()
        for arg in args :
            print(arg, end=" ")
        print()
        self.prt.release()

    def send_exch(self,msg,name,i):
            self.myprint(name," sender acquire empty ")
            msg.empty.acquire()

            msg.buf[0]="hi " + name +str(i)
            # time.sleep(2)

            self.myprint(name," sender release  full i= ",i)
            msg.full.release()
            # time.sleep(1)


    def sender(self,msg,name):
        self.myprint("sender", name)
        n=3
        for i in range(n):
            self.send_exch(msg,name,i)

        self.myprint(name, "sender finished")

    
    def sender_cnd(self,msg,name):
        self.myprint("sender", name)
        n=3
        for i in range(n):
            # self.myprint(name," sender  acquire")
            msg.avail.acquire()
            # self.myprint(name," sender got acquire")

            self.send_exch(msg,name,i)
            # self.myprint(name," sender  release")
            msg.avail.release()
            time.sleep(random.random()/10)
        self.myprint(name, "sender finished")


    def receiver(self,msg):
        self.myprint("receiver")
        while True:
            self.myprint("R  receiver release empty  ")
            msg.empty.release()

            self.myprint("R  receiver acquire full ")
            msg.full.acquire()            

            self.myprint("----------------------------",msg.buf )
            if[buf[0]=="stop"]:
                break
            # time.sleep(1)


            

    def ping(self):
        msg=msg_t(self)
        t1=threading.Thread(target=self.sender,args=(msg,"s1 "))
        t1.start()
        # t2=threading.Thread(target=self.sender,args=(msg,"s2 "))
        # t2.start()
        tr=threading.Thread(target=self.receiver,args=(msg,))
        tr.start()
    
    def ping_cnd(self):
        msg=msg_t(self)
        t1=threading.Thread(target=self.sender_cnd,args=(msg,"s1 "))
        t1.start()
        # time.sleep(2)
        tr=threading.Thread(target=self.receiver,args=(msg,))
        tr.start()
        t2=threading.Thread(target=self.sender_cnd,args=(msg,"s2 "))
        t2.start()
    
      

test1=test_t()
# test1.ping()
test1.ping_cnd()



# xlist=[1]
# x=1

# def t(vlist,v):
#     vlist=[8,8]
#     v=9

# t(xlist,x)
# self.myprint(xlist,x)