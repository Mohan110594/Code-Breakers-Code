using Memoization:
#Time -->o(mn)
#space -->o(mn)

class Solution(object):
    def __init__(self):
        self.dirs=[[1,0],[0,1]]
        
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid)==0:
            return 0
        if obstacleGrid[0][0]==1:
            return 0
        memo=[[-1 for i in range(len(obstacleGrid[0]))]for j in range(len(obstacleGrid))]
        return self.dfs(obstacleGrid,memo,0,0)
        
        
        
    def dfs(self,obstacleGrid,memo,start,end):
        # print(memo,start,end)
        if start==len(obstacleGrid)-1 and end==len(obstacleGrid[0])-1:
            return 1
        if memo[start][end]!=-1:
            return memo[start][end]
        count=0
        for pos in self.dirs:
            dx=start+pos[0]
            dy=end+pos[1]
            if 0<=dx<len(obstacleGrid) and 0<=dy<len(obstacleGrid[0]) and obstacleGrid[dx][dy]!=1:
                count+=self.dfs(obstacleGrid,memo,dx,dy)
                
        memo[start][end]=count
        return count

DP:

#Time -->o(mn)
#space -->o(mn)

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        out=[[None for i in range(len(obstacleGrid[0]))]for j in range(len(obstacleGrid))]
        # print(out)
        if obstacleGrid[0][0]==1:
            return 0
        place=1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                place=0
                out[i][0]=place
            else:
                out[i][0]=place
        place=1
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j]==1:
                place=0
                out[0][j]=place
            else:
                out[0][j]=place
            
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    out[i][j]=out[i-1][j]+out[i][j-1]
                else:
                    out[i][j]=0
        # print(out)
        return out[len(obstacleGrid)-1][len(obstacleGrid[0])-1]