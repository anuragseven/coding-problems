# Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        result=[]
        maxLevel=[0]
        self.rv(root,result,maxLevel,1)
        return result

    def rv(self,root,result,maxLevel,level):
        if root is None:
            return
        if maxLevel[0]<level:
            result.append(root.data)
            maxLevel[0]=level
        self.rv(root.right,result,maxLevel,level+1)
        self.rv(root.left,result,maxLevel,level+1) 