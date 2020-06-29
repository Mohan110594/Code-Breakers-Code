DFS:

#Time comp --> o(n)
#space comp --> o(log n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def helper(self,root,mini,maxi):
        if root==None:
            return True
        if root.val<mini or root.val>maxi:
            return False
        
        return self.helper(root.left,mini,root.val-1) and self.helper(root.right,root.val+1,maxi)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        mini=float('-inf')
        maxi=float('inf')
        
        return self.helper(root,mini,maxi)
        
        
        
 BFS:
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root==None:
            return True
        
        queue=deque([[root,float('-inf'),float('inf')]])
        
        while len(queue)>0:
            val=queue.popleft()
            node=val[0]
            mini=val[1]
            maxi=val[2]
            
            if node.val<mini or node.val>maxi:
                return False
            
            if node.left!=None:
                queue.append([node.left,mini,node.val-1])
            
            if node.right!=None:
                queue.append([node.right,node.val+1,maxi])
                
        return True