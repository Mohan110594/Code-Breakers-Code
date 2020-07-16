#Time comp --> o(mn)
#space comp --> o(mn)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1 for i in range(n)]for j in range(m)]
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                
        return dp[len(dp)-1][len(dp[0])-1]
        