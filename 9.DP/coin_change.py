#DP
#Time comp --> o(mn)
#space comp --> o(mn)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[0 for i in range(amount+1)]for j in range(len(coins)+1)]
        
        for i in range(len(coins)):
            dp[i][0]=0
            
        for j in range(1,len(dp[0])):
            dp[0][j]=float('inf')
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j<coins[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
                    
        # print(dp)
                    
        if dp[len(dp)-1][len(dp[0])-1]==float('inf'):
            return -1
                    
        return dp[len(dp)-1][len(dp[0])-1]