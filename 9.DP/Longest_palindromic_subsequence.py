#Time comp --> o(n2)
#space comp --> o(n2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        dp=[[0 for i in range(len(s))]for j in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i]=1
        
        # This is similar to matrix multiplication problem where we fill only half of the matrix
        # watch https://www.youtube.com/watch?v=_nCsPn7_OgI&t=27s for more understanding
        # elements are filled in diagonal order
        
        for i in range(len(dp)-2,-1,-1):
            
            
            for j in range(i+1,len(dp[0])):
                
                # if the characters are same then we count 2 + recurse on the remaining string
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i+1][j-1]
                    
                else:
                    # If the characters dont match then we take the max from the previous and the below one.
                    
                    # i.e in bbbab
                    # we compare b at index 0 with b at index len(s)-1 both are equal so we check for s[1:len(s)-2]
                    
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
                    
        return dp[0][len(dp[0])-1]
                
        
        