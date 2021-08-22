

class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        q=[]
        l=[]
        q.append(root)
        l.append(root.data)
        
        while q!=[]:
            v=q.pop(0)
            if v.left is not None:
                q.append(v.left)
                l.append(v.left.data)
            
            if v.right is not None:
                q.append(v.right)
                l.append(v.right.data)
        
        return l