# Given two strings A and B. Find the characters that are not common in the two strings. 
def UncommonChars(A, B):
        s1=set(A)
        s2=set(B)
        commons=''
        for c in s1:
            if c not in s2:
                commons+=c
        
        for c in s2:
            if c not in s1:
                commons+=c
        
        return ''.join(sorted(commons)) if commons!='' else -1