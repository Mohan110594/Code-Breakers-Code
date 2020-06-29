#DFS
#Time comp --> o(n)
#space comp --> o(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.sum1=0
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        self.helper(root,0)
        return self.sum1
        
    def helper(self,root,value):
        
        if root==None:
            return
        
        if root.left==None and root.right==None and value==1:
            self.sum1+=root.val
        
        self.helper(root.left,1)
        self.helper(root.right,2)
        
        
#BFS

#Time comp --> o(n)
#space comp --> o(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        
        queue=deque([[root,0]])
        out=0
        while len(queue)>0:
            val=queue.popleft()
            node=val[0]
            value=val[1]
            
            if value==1 and node.left==None and node.right==None:
                # print(node.val)
                out+=node.val
            
            if node.left!=None:
                queue.append([node.left,1])
                
            if node.right!=None:
                queue.append([node.right,2])
        
        return out
        