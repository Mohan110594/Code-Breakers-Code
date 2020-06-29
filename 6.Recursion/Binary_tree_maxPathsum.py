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
        self.out=float('-inf')
    
    def dfs(self,root):
        if root==None:
            return 0
        
        # we are trying to take the max on both the left and right sub trees
        left_sum=max(self.dfs(root.left),0)
        right_sum=max(self.dfs(root.right),0)
        
        # max sub tree sum can be not including the root of the tree
        val=left_sum+right_sum+root.val
        # storing the max path value which doesnot contain the root 
        self.out=max(self.out,val)
        # If in case the root path is chosen then take the max values out of left and right sub trees
        return root.val+max(left_sum,right_sum)        
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        out=float('-inf')
        self.dfs(root)
        
        return self.out
        

        