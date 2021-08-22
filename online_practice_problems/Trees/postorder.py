

def postOrder(root):
    l=[]
    post(root,l)
    return l

def post(root,l):
    if root is None:
        return 
    post(root.left,l)
    post(root.right,l)
    l.append(root.data)