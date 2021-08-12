def findMaxForN(root,N):
    return search(root,N)
    
    
def search(root,N):
    if root is None :
        return -1
    
    if root.key==N:
        return N
    if root.key<N:
        v=search(root.right,N)
        if v==-1:
            return root.key
        else:
            return v
    
    else:
        return search(root.left,N)