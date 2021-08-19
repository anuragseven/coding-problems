# You are given a string S, the task is to reverse the string using stack.

def reverse(S):
    
    stack=[]
    for c in S:
        stack.append(c)
    
    result=''
    while stack!=[]:
        result+=stack.pop()
    return result