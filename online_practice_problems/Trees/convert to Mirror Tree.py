# Given a Binary Tree, convert it into its mirror.
# image: https://contribute.geeksforgeeks.org/wp-content/uploads/mirrortrees.jpg
class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        if root is None:
            return  
        
        temp=root.right
        root.right=root.left
        root.left=temp
        self.mirror(root.left)
        self.mirror(root.right)