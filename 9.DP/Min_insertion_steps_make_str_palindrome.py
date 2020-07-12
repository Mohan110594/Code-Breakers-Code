#Time comp --> o(n2)
#space comp --> o(n2)

class Solution:
    def minInsertions(self, s: str) -> int:
        
        dp=[[0 for i in range(len(s))]for j in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i]=1
            
        for start in range(len(s)-1,-1,-1):
            for end in range(start+1,len(s)):
                
                if s[start]==s[end]:
                    dp[start][end]=2+dp[start+1][end-1]
                    
                else:
                    
                    dp[start][end]=max(dp[start][end-1],dp[start+1][end])
                    
        return len(s)-dp[0][len(dp[0])-1]
        