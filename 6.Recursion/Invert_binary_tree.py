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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return
        
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        
        root.left=right
        root.right=left
        
        return root
        
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return root
        
        queue=deque([root])
        
        
        while len(queue)!=0:
            node=queue.popleft()
            if node==None:
                continue
            
            if node.left!=None:
                queue.append(node.left)
            else:
                queue.append(None)
            if node.right!=None:
                queue.append(node.right)
            else:
                queue.append(None)
            node.right,node.left=node.left,node.right
                
        return root
                
        
        