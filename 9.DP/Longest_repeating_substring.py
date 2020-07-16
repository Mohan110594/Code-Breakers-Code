#DP
#Time comp --> o(n2)
#space comp --> o(n2)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        
        dp=[[0 for i in range(len(S)+1)] for j in range(len(S)+1)]
        
        maxlen=0
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if S[i-1]==S[j-1] and i!=j:
                    dp[i][j]=1+dp[i-1][j-1]
                    
                    maxlen=max(maxlen,dp[i][j])
                
        # print(dp)
                
        return maxlen
                           
        