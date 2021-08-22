# Given a Binary Tree with all unique values and two nodes value n1 and n2. The task is to find the lowest common ancestor of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them is present. 

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        if root is None :
            return 
        
        if root.data==n1 or root.data==n2:
            return root
        
        l=self.lca(root.left,n1,n2)
        r=self.lca(root.right,n1,n2)
        
        if l and r:
            return root
        
        return l if l is not None else r