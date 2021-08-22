# Given a Binary Tree, your task is to find its level order traversal.
# For the below tree the output will be 1 $ 2 3 $ 4 5 6 7 $ 8 $.


def levelOrder(root):
    result=[]
    result.append([root.data])
    bfs(root,result)
    return result
def bfs(root,result):
    
    
    q=[]
    part=[]
    q.append(root)
    
    while q:
        
        count=len(q)
       
        
        
        while count>0:
            v=q.pop(0)
            if v.left is not None:
                part.append(v.left.data)
                q.append(v.left)
            if v.right is not None:
               part.append(v.right.data)
               q.append(v.right)
            count-=1
        if part:
            result.append(part)
            part=[]