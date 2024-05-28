


class HashMap():
            # You can change the constructor anyway you want
    def __init__(self):
        self.mx=1000
        self.nlocks=self.mx/1
        self.lst=[[]]*self.mx
        self.max_ar=0
        self.lk=sem()

    def put(self, key: str, value: str):
        self.lk.lock()
        h=hash(key)
        h1=h % self.mx

        ar=self.lst[h1][:]
        pair=(key, value)

        ip2=None
        for ip, pair in enumerate(ar):
            key2=pair[0]
            if key == key2:
                ip2=ip
                break
        if ip2 is None:
            ar.append(pair)
        else:
            ar[ip2]=pair

        self.lst[h1]=ar[:]
        self.lk.ulock()
        return

        # TODO

    def get(self, key) -> str:
        value=None
        h=hash(key)
        h1=h % self.mx
        ar=self.lst[h1]
        for pair in ar:
            key2=pair[0]
            if key == key2:
                value=pair[1]
                break
        return value

        # TODO
        