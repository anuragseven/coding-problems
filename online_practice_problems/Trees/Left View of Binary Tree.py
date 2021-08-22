# Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.
# image:https://media.geeksforgeeks.org/wp-content/cdn-uploads/left-view.png

def LeftView(root):
    result=[]
    maxLevel=[0]
    lv(root,result,maxLevel,1)
    return result

def lv(root,result,maxLevel,level):
    if root is None:
        return
    if maxLevel[0]<level:
        result.append(root.data)
        maxLevel[0]=level
    lv(root.left,result,maxLevel,level+1)
    lv(root.right,result,maxLevel,level+1)   