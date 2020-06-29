#Time comp -> o(n)
#space comp --> o(n)

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root==None:
            return root
        ans=0
        queue=deque([[root,0]])
        
        while len(queue)!=0:
            size=len(queue)
            
            for i in range(size):
                val=queue.popleft()
                
                node=val[0]
                count=val[1]
                
                if node.left!=None:
                    queue.append([node.left,(2*count)+1])
                if node.right!=None:
                    queue.append([node.right,(2*count)+2])
                    
                if i==0:
                    mini=count
                
                if i==size-1:
                    maxi=count
                    
            ans=max(ans,maxi-mini+1)
        return ans