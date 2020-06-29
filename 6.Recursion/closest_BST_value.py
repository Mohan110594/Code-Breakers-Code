#DFS:
#Time comp --> o(log n)
#soace comp --> o(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.closest=float('inf')
        self.closest_value=0
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root==None:
            return 0
        
        self.dfs(root,target)
        
        return self.closest_value
        
    def dfs(self,root,target):
        
        if root==None:
            return 
        
        if self.closest>abs(target-root.val):
            self.closest=abs(target-root.val)
            self.closest_value=root.val
            
        if target>root.val:
            self.dfs(root.right,target)
            
        else:
            self.dfs(root.left,target)
            
#BFS
#Time comp --> o(log n)
#space comp --> o(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root==None:
            return 0
        
        closest=float('inf')
    
        
        while root:
            if closest>abs(target-root.val):
                closest=abs(target-root.val)
                closest_node=root.val
            
            if target>root.val:
                root=root.right
                
            else:
                root=root.left
        return closest_node
