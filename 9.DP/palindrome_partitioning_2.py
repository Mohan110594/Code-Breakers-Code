#Time comp --> o(n2)
#space comp --> o(n2)

class Solution:
    
    def palindrome(self,s,start,end):
        
        return s[start:end+1]==s[start:end+1][::-1]
    
    def minCut(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        
        dp=[[False for i in range(len(s))]for j in range(len(s))]
        
        
        # First create a dp matrix which has cells which represents the  start and end indices of the string where string is palindrome.
        # similar to longest palindromic substring except for  ot including the logic for calculating maxlen at every palindromic point
        
        for i in range(len(s)):
            dp[i][i]=True
        
        
        for start in range(len(s)-1,-1,-1):
            
            for end in range(start+1,len(s)):
                
                if s[start]==s[end]:
                    if end-start==1 or dp[start+1][end-1]:
                        dp[start][end]=True
                        
                        
        # we have a cut array to store the min cuts at every point
        cut=[0 for i in range(len(s))]
        
#         1.traverse the dp matrix from last to front.
#         2.when found true it means there is a palindrome string at that start and end indices.
#         3.when end==len(s)-1 it means that the whole string is palindrome.
#         4.else we take the min cuts required for the given string.
        
#         use the example 'abdbc' for better understanding.
#         First create the palindrome matrix and then go step by step, will be easy to understand.
        
        for start in range(len(s)-1,-1,-1):
            
            mincuts=len(s)
            
            for end in range(len(s)-1,start-1,-1):
                
                if dp[start][end]:
                    
                    if end==len(s)-1:
                        mincuts=0
                    else:
                        mincuts=min(mincuts,1+cut[end+1])
                        
            cut[start]=mincuts
            
        return cut[0]
                

                    
                    
                    
                    
                    
        