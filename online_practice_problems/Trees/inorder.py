

class Solution:
    def InOrder(self,root):
        l=[]
        self.inorder(root,l)
        return l
    
    def inorder(self,root,l):
        if root is None:
            return
        self.inorder(root.left,l)
        l.append(root.data)
        self.inorder(root.right,l)