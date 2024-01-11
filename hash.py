# s_set={1,2}
# s_set.add(44)
# for s in s_set:
#     print(s)
# print(len(s_set))

# s_map={"m1":1, "m2":2 }
# s_map["m3"]=3
# del s_map["m3"]
# s_map.pop("m2")
# for s in s_map.items():
#     print(s)

s_list=[1,2,3]
# s_list.append(4)
# print(s_list)
# for i in range(len(s_list)-1, -1, -1):
#     print(i,   s_list[i])
# print(s_list[-3:-1])

class mysort:
    def __init__(self) -> None:
        pass

    def swap(self, s_list, m, n):
        print(f"swap {m} {n}")
        x=s_list[m]
        s_list[m]=s_list[n]
        s_list[n]=x
        print(f"after {s_list}")


    def buble(self, s_list):

        while True:
            i=0
            nswap=0
            while i< len(s_list)-1:
                if s_list[i+1] < s_list[i]:
                    self.swap(s_list, i, i+1)
                    nswap+=1
                i+=1

            if nswap == 0:
                break


m1=mysort()
s_list=[-22,1,-1, -22, 1]
m1.buble(s_list)
print(s_list)