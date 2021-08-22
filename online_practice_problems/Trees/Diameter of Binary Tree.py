# Given a Binary Tree, find diameter of it.
# The diameter of a tree is the number of nodes on the longest path between two end nodes in the tree. The diagram below shows two trees each with diameter nine, the leaves that form the ends of a longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes).
# image: https://contribute.geeksforgeeks.org/wp-content/uploads/diameter.jpg
class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        result=[]
        result.append(-1)
        
        self.height(root,result)
        return result[0]
    
    
    def height(self,root,result):
        if root is None:
            return 0
        
        l=self.height(root.left,result)
        r=self.height(root.right,result)
        
        result[0]=max(result[0],1+l+r)
        return 1+max(l,r)