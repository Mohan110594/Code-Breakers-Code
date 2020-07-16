#Time comp --> o(mn)
#space comp --> o(mn)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s3)!=len(s2)+len(s1):
            return False
        
        dp=[[False for i in range(len(s2)+1)]for j in range(len(s1)+1)]
        
        dp[0][0]=True
        
        # print(dp)
        
        # row wise fill
        
        for i in range(1,len(dp[0])):
            if s2[i-1]==s3[i-1] and dp[0][i-1]==True:
                dp[0][i]=True
                
        # col wise fill
        
        for i in range(1,len(dp)):
            if s1[i-1]==s3[i-1] and dp[i-1][0]==True:
                dp[i][0]=True
                
                
        # remaining row fill
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                # we need to start in s3 from this index
                index=i+j-1
                # let s1 is on row side and s2 is on col side
                # if char in s3 is equal to char in s1 then we check prev value along the col side for the current value
                # if char in s3 is equal to char in s2 then we check prev value along the row side for the current value
                
                if s3[index]==s1[i-1] and dp[i-1][j]==True:
                    dp[i][j]=True
                    
                elif s3[index]==s2[j-1] and dp[i][j-1]==True:
                    dp[i][j]=True
                    
                    
        return dp[len(dp)-1][len(dp[0])-1]
                    
                
            
        
        