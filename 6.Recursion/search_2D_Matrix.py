#Time comp --> o(m+n)
#space comp --> o(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix)==0:
            return False
        row=0
        col=len(matrix[0])-1
        
        while 0<=row<len(matrix) and 0<=col<len(matrix[0]):
            if matrix[row][col]==target:
                return True
            elif target>matrix[row][col]:
                row=row+1
            else:
                col=col-1
                
        return False
        