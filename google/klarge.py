class test:
    def __init__(self,k, lst) -> None:
        self.k=k
        self.lst=[lst[0]]
        for i in range(1,len(lst)):
            self.add(lst[i])

        pass

    def add(self ,n ):

        # at the end
        if n > self.lst[-1]:
            self.lst.append(n)
            #truncate if needed
            if len(self.lst)> self.k:
                self.lst=self.lst[-self.k:]
        else:
            # insert into rigth slot of already sorted .reject duplicates
            for i in range(len(self.lst)-1):
                if n == self.lst[i] or n== self.lst[i+1]:
                    break
                if self.lst[i] < n and n < self.lst[i+1]:
                    #shift
                    for j in range(i):
                        self.lst[j]=self.lst[j+1]
                    self.lst[i]=n
                    break
        return self.lst[0]

t=test(2, [4,3,6])
# print(t.add(6), t.lst)
# print(t.add(2), t.lst)
print(t.add(7), t.lst)