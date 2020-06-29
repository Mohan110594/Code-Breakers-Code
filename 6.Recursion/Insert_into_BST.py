#DFS
#Time comp --> o(log n)
#space comp --> o(log n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root==None:
            return TreeNode(val)
        
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        elif val<root.val:
            root.left=self.insertIntoBST(root.left,val)
        
        return root
        
#BFS
#Time comp --> o(logn)
#space comp --> o(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root==None:
            return TreeNode(val)
        
        node=root
        
        while node:
            
            if val>node.val:
                
                if node.right==None:
                    node.right=TreeNode(val)
                    break
                else:
                    node=node.right
                    
            else:
                
                if node.left==None:
                    node.left=TreeNode(val)
                    break
                else:
                    node=node.left
                
        
        return root