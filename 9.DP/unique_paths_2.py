#Time comp --> o(n2)
#space comp --> o(n2)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp=[[0 for j in range(len(obstacleGrid[0]))]for j in range(len(obstacleGrid))]
        
        if obstacleGrid[0][0]==1:
            return 0
        
        place=1
        #Be careful with the edge cases.once we get a 1 along the path in the first row and col we cannot move forward in that position
        for i in range(len(dp)):
            
            if obstacleGrid[i][0]==1:
                place=0
                dp[i][0]==place
                
            elif obstacleGrid[i][0]==0:
                dp[i][0]=place
                
        place=1        
        
        for j in range(len(dp[0])):
            if obstacleGrid[0][j]==1:
                place=0
                dp[0][j]==place
            
            elif obstacleGrid[0][j]==0:
                dp[0][j]=place
                
                
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                    
                
                    
        return dp[len(dp)-1][len(dp[0])-1]
        
        