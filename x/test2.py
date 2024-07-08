# You devise an abstraction for this, called a "multi-semaphore".

# A multi-semaphore is initialized with a mapping of resource identifiers to a count of how many of the resource is available.

# A multi-semaphore allows callers to acquire access to resources by passing a collection of resource identifiers to an `acquire` method.
# Upon acquisition, a caller is presented with a permit. 
# When the caller invokes `release` on the permit, the resources are returned to the system.


import threading
import time

class Permit:
    def __init__(self, ids, ms):
        self.ids=ids
        # save MultiSemaphore object
        self.ms=ms
        return
     
    def release(self, thrid):
        self.ms.release(self.ids, thrid)
        return


class MultiSemaphore:
    def __init__(self,initialPermits: dict[str, int]):
        self.dd=initialPermits
        self.glock=threading.Lock()    # to protect scan operations
        self.tsem_list=[]             # to keep list of thread lsemaphores
        pass

    def acquire(self, ids: list[str], thrid) -> Permit:
        #  create thread lock and append to list
        tsem=threading.Semaphore(0)
        self.tsem_list.append(tsem)
        while True:
            # relese global and wait for  thread lock
            #re-aquire glocbal and scan
            self.glock.acquire()
            good=True
            #  check resources
            for id in ids:
                if self.dd[id]==0:
                    good=False
                    break
            if good:
                # ajust counts
                for id in ids:
                    self.dd[id]-=1
                # build permit object
                p=Permit(ids, self)
                self.tsem_list.remove(tsem)
                self.glock.release()
                return p
            else:
                # todo check for globl timeout and break -> return err
                self.glock.release()
                print("sem in thread ", thrid, "taking" ,tsem)
                tsem.acquire()                    
        return 

    def release(self, ids, thrid):
        # get global lock
        self.glock.acquire()
        # ajust resources
        for id in ids:
            self.dd[id]-=1
        # release all thread locks to allow them to recheck
        for tlock in self.tsem_list:
            print("sem in thread ", thrid, "release" ,tlock)
            tlock.release()
        self.glock.release()
        return 
    
    
def test(m, thrid, ids):
    print("thrid",thrid," acquire started ", ids)
    time0=time.time()
    p=m.acquire(ids,thrid)
    time_diff = (time.time() - time0) * 1000
    print("thrid",thrid," acquire  ended and lasted  ", ids, f"{time_diff:.6f}", "milliseconds")
    print("thrid",thrid," sleep started ")
    time.sleep(5) 
    print("thrid",thrid," sleep ended ")
    p.release(thrid)
    print("thrid",thrid," released ", ids)
    return
    
            
dd={"aa":1,"bb":1}
m=MultiSemaphore(dd)

#  start thread1 . 
t1 = threading.Thread(target=test, args=(m, 1,["aa"] ))
t1.start()

#  start thread2 . different resource . should not block 
time.sleep(1)
t2 = threading.Thread(target=test, args=(m, 2,["bb"] ))
t2.start()

# contiue with main thread . should block 
time.sleep(1)
test(m,0 ,["aa"])

print("end")

    
