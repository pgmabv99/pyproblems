
class t:

    def draw(self, scr, w, y, x1, x2):

        bi1=(y-1)*w + x1
        bi2=(y-1)*w + x2
        by1=floor(bi1/8)
        by2=floor(bi2/8)
        if by2>by1+1:
            #fill full 1111... bytes for in btween 
            for i in range(by1+1,by2):
                scr[i]=byte(-1)  #assume python has a similiar 
                
        #partial
        r1=bi1%8
        r1x=8-r1
        z=2**(r1x+1)-1    #all ones
        scr[by1]=byte(z)

        r2=bi2%8
        r2x=8-r2
        z=(-1)<<r2x
        scr[by2]=byte(z)

