import math
class node:

    def __init__(self,pv):
        self.v=pv
        self.next=None

    def list_2_num(self):
        if self.next==None :
            return self.v, 1
        else :
            next=self.next
            num,pos=next.list_2_num()
            numa=self.v*(10**pos)
            pos2=pos+1
            # print(pos2,numa)
            num2=num+numa
            return num2, pos2

    def swap(self, nodex):
        z=nodex.next
        nodex.next=self.next
        self.next=z

class slist:
    def __init__(self):
        self.first=None

    def add_f(self,node):
        node.next=self.first
        self.first=node


    def show(self):
        node=self.first
        while (node!=None):
            print(node.v,end="->")
            node=node.next
        print()

    def list_2_num(self):
        nodex=self.first
        num,pos=nodex.list_2_num()
        # print("final", num, pos)
        return num

    def num_2_list(self, num):
        num1=num%10
        self.first=node(num1)
        num2=math.floor(num/10)
        prev=self.first
        while num2>0:
            num1=num2%10
            num2=math.floor(num2/10)
            new=node(num1)
            prev.next=new
            prev=new

    def rev(self,n,m):
        print ("n,m", n, m)
        beg=None
        if n>1:
            x_cur=self.first
            i=1
            while i< n-1:
                x_cur=x_cur.next
                i=i+1
            n_node=x_cur
        else:
            beg=node(-999)
            beg.next=self.first
            n_node=beg
        x_cur=n_node.next
        x_next=x_cur.next
        print("n_node",n_node.v)
        print("cur",x_cur.v)
        print("next",x_next.v)

        i=n+1
        while i<m+1:

            if x_next==None:
                print("reached end at", i )
                break
            n_node.next=x_next
            z=x_next.next
            x_next.next=x_cur
            #new end
            if i==n+1:
                #1st creat end node, remember it 
                x_cur.next=None
                x_end=x_cur
            #next step
            x_cur=x_next
            x_next=z
            i=i+1
        #hook up end to rest of list
        x_end.next=x_next
        if beg!=None:
            self.first=beg.next
            del(beg)
        


# s1=slist()
# s1.add_f(node(0))
# s1.add_f(node(2))
# s1.add_f(node(3))
# s1.show()
# num1=s1.list_2_num()
# print("num1",num1)

# s2=slist()
# s2.add_f(node(0))
# s2.add_f(node(0))
# s2.add_f(node(1))
# s2.show()
# num2=s2.list_2_num()
# print("num2",num1)

# s3=slist()
# num3=num1+num2

# s3.num_2_list(num3)

# print(num3)
# print("final list")
# s3.show()

s4=slist()
xlist=[6,5,4,3,2,1]
for x in xlist:
  s4.add_f(node(x))
s4.show()
s4.rev(1,7)
s4.show()