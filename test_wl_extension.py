import sys

class ext:
    def __init__(self,fw,tw,ws):
        self.output = []
        self.ws = ws
        self.fw = fw
        self.tw = tw
        self.used = []
    def derive_first_last(self,word,chk):
        assert len(word) == len(chk)
        count = len(chk)
        for i in range(len(chk)):
            if word[i] == chk[i]:
                count -=1
        if count == 1:
            return True
    def test(self,fw):
        ws = self.ws
        used = self.used
        assert len(fw) == len(tw)
        for word in ws:
            if word in used:
                continue
            if word == fw:
                self.output.append(word)
                return self.output
            if len(word) == len(fw):
                chk = len(fw)
                for i in range(len(fw)):
                    if fw[i] == word[i]:
                        chk -=1
                if chk == 1:
                    chk = len(fw)
                    self.output.append(word)
                    used.append(word)
                    self.test(word)
        return self.output

def test2(fw,ws):
    alpha = "abcdefghijklmnopqrstuvwxyx"
    output = []
    found = False
    length = len(fw)
    if len(ws) == 0:
        return[]
    for i in range(length):
        for letter in alpha:
            if fw.replace(fw[i],letter) in ws:
                fw = fw.replace(fw[i],letter)
                output.append(fw)
                ws.remove(fw)
                found = True
                break
        if found == True:
            break
        else:
            continue
    return ws
lst = ["sown","soot","slot", "soon"]
lst = set(lst)
var = test2('slow',lst)
print(var)


