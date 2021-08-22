# Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        if root is None:
            return 1
        if root.left is None and root.right is None :
            return 1
            
        r=0
        
        if root.left is not None and root.right is not None:
            r=root.data==(root.left.data+root.right.data)
        
        if root .left is None:
            r=(root.data==root.right.data)
        
        if root.right is None:
            r=(root.data==root.left.data)
        
        if r:
            return 1 if (r and self.isSumProperty(root.left) and self.isSumProperty(root.right)) else 0
        else:
            return 0