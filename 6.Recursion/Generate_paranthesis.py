#Time comp -->
#space comp -->


class Solution(object):
    
    def __init__(self):
        self.out=[]
    
    def backtrack(self,str1,left,right,n):
        
        if left>n or right>n:
            return
        
        if left==right==n and len(str1)==(2*n):
            self.out.append(str1)
        
        if left<n:
            self.backtrack(str1+'(',left+1,right,n)
        if right<left:
            self.backtrack(str1+')',left,right+1,n)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.backtrack('',0,0,n)
        return self.out