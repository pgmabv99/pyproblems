from enum import Enum
class sect:
    def __init__(self):
        self.type=None  

        self.str=None 

class sect_t(Enum):
    CONST=0
    FIXED=1
    VAR=2
    VARRPT=3

class p:

    def parse_pat(self,pat):
        p.psect_list=[]
        i=0
       
        while i<len(pat):
            psect=sect()

            if pat[i]=="?":
                psect.type=sect_t.FIXED
                i=i+1
            elif pat[i]=="*":
                psect.type=sect_t.VAR
                i=i+1
            elif pat[i]==".":
                psect.type=sect_t.VARRPT
                i=i+1
            else :
                #add char section
                psect.type=sect_t.CONST
                j=i
                #add next char substring
                while j< len(pat):
                    if pat[j] in ["*","?","."] :
                        break
                    j=j+1
                psect.str =pat[i:j]
                i=j               
           
            p.psect_list.append(psect)

    def check_pat(self):
        valid=True
        for k in range(len(p.psect_list)):
            psect=p.psect_list[k]
            print ("pat type",psect.type, "str", psect.str)
            if  psect.type==sect_t.VAR and \
                k+1<len(p.psect_list) and \
                p.psect_list[k+1].type!=sect_t.CONST :
                    print("err .. variable mask must be followed by const string")
                    valid=False
            if  (psect.type==sect_t.VARRPT) :
                if  k==0  : 
                    print("err .. variable REPEAT mask cannot be pos 0")
                    valid=False
                else:
                    if p.psect_list[k-1].type!=sect_t.CONST :
                        print("err .. variable repeat  mask must  follow const string")
                        valid=False

        return valid
                


    def parse_text(self,text):

        match=True
        i=0
        for k in range(len(p.psect_list)):
            psect=p.psect_list[k]
            if psect.type==sect_t.CONST:
                lstr=len(psect.str)
                if i+lstr >len(text):
                    match=False
                    break
                if text[i:i+lstr] !=psect.str:
                    match=False
                    break
                i=i+lstr
            elif psect.type==sect_t.FIXED:
                if i+1 >len(text):
                    match=False
                    break
                i=i+1
            elif psect.type==sect_t.VAR:
                if k==len(p.psect_list)-1:
                    #last variable section . any text including empty matches
                    i=len(text)
                    continue
                else :
                    #look for the next char sect
                    str1=p.psect_list[k+1].str
                    lstr1=len(str1)
                    j=i
                    found=False
                    while j+lstr1<=len(text):
                        str2=text[j:j+lstr1]
                        # print(str2)
                        if str2==str1:
                            found=True
                            break
                        j=j+1
                    if found==False:
                        match=False
                        break
                    i=j
                    continue
            elif psect.type==sect_t.VARRPT:
                #last char of prev string
                char1=p.psect_list[k-1].str[-1]
                j=i
                match_char1=True
                while j<len(text):
                    if text[j]!=char1:
                        match_char1=False
                        break
                    j=j+1
                i=j
        if i<len(text):
            print("left over ", text[i:])
            match=False
        return match


p1=p()


pat="c.*x"

p1.parse_pat(pat)
if len(p.psect_list)==0 :
    exit()
if p1.check_pat()!=True:
    print("err: invalid pattern skipping")
    exit()
text="cccaaax"

print(pat)
print(text)
match=p1.parse_text(text)

print(match)



                
                
