#DFS
#Time comp --> o(n)
#space comp --> o(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        
        return self.dfs(root,0,sum)
        
        
    def dfs(self,root,sum1,sum):
        
        if root==None:
            return False
        
        
        sum1=sum1+root.val
        
        
        if sum1==sum and root.left==None and root.right==None:
            return True
        
        return self.dfs(root.left,sum1,sum) or self.dfs(root.right,sum1,sum)

#BFS

#Time comp --> o(n)
#space comp --> o(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        queue=deque([[root,root.val]])
        
        while len(queue)>0:
            value=queue.popleft()
            node=value[0]
            sum1=value[1]
            
            if sum1==sum and node.left==None and node.right==None:
                return True
            
            if node.left!=None:
                queue.append([node.left,sum1+node.left.val])
                
            if node.right!=None:
                queue.append([node.right,sum1+node.right.val])
                
        return False