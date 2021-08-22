# Given a binary tree, find if it is height balanced or not. 
# A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

class Solution:
    def isBalanced(self,root):
            
        l=self.height(root.left)
        r=self.height(root.right)
         
        if type(l)==bool or type(r)==bool:
            return False
        return abs(l-r)<=1
    
    
    def height(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
            
        l=self.height(root.left)
        r=self.height(root.right)
         
        if type(l)==bool or type(r)==bool:
            return False
             
        if abs(l-r)<=1:
            return 1+max(l,r)
        
        return False