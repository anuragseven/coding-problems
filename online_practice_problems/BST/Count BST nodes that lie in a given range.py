#Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.
def getCount(root,low,high):
    return countNodes(root,low,high)


def countNodes(root,low,high):
    if root is None:
        return 0
    
    if low<=root.data<=high:
        
        return 1+ countNodes(root.left,low,high)+countNodes(root.right,low,high)
    
    elif root.data<low:
        return countNodes(root.right,low,high)
    
    elif root.data>high:
        return countNodes(root.left,low,high)