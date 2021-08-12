def isPlaindrome(S):
    return 1 if  S==S[::-1] else 0


def isPlaindrome(S):
    n=len(S)//2
    l=len(S)-1
    i=0
    while n>=0:
        if S[i]!=S[l-i]:
            return 0
	n-=1
        i+=1
    return 1