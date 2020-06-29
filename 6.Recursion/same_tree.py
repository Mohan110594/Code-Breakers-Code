
#DFS
#Time comp --> o(n)
#space comp --> o(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True 
        if q==None or p==None:
            return False
        
        if p.val!=q.val:
            return False
        
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        

#BFS
#TIme --> o(n)
#space --> o(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        
        queue=deque([[p,q]])
        
        while len(queue)>0:
            val=queue.popleft()
            p1=val[0]
            q1=val[1]
            if p1==None or q1==None:
                return False
            if p1.val!=q1.val:
                return False
            
            if p1.left!=None or q1.left!=None:
                queue.append([p1.left,q1.left])
            if p1.right!=None or q1.right!=None:
                queue.append([p1.right,q1.right])
            
        return True