
def preorder(root):
    l=[]
    pre(root,l)
    return l

def pre(root,l):
    if root is None:
        return
    l.append(root.data)
    pre(root.left,l)
    pre(root.right,l)