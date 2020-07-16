#DP
#Time comp --> o(mn)
#space comp --> o(mn)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        maxlen=0
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    
                else:
                    
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                  
                maxlen=max(maxlen,dp[i][j])
                    
        return maxlen
                    
 #DP
#Time comp --> o(mn)
#space comp --> o(n)      
       
 class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for i in range(len(text2)+1)] for j in range(2)]
        maxlen=0
        
        for i in range(1,len(text1)+1):
            for j in range(1,len(dp[0])):
                if text1[i-1]==text2[j-1]:
                    dp[i%2][j]=1+dp[(i-1)%2][j-1]
                    
                else:
                    
                    dp[i%2][j]=max(dp[(i-1)%2][j],dp[i%2][j-1])
                  
                maxlen=max(maxlen,dp[i%2][j])
                
            # print(dp)
                    
        return maxlen
                    
