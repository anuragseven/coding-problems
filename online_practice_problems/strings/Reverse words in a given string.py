#Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

def reverseWords(self,S):
        word=''
        l=[]
        for w in S:
            if w=='.':
                if word!='':
                    l.append(word)
                    l.append('.')
                word=''
            
            else :
                word+=w
        if word!='':
            l.append(word)
        return ''.join(l[::-1])