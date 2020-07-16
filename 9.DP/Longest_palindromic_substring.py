#Expand around the center

#Time comp --> o(n2)
#space comp --> o(1)

class Solution:
    
    def __init__(self):
        self.inital=0
        self.maxlen=0
    
    def palindromesub(self,start,end,s):
        
        while start>=0 and end<len(s):
            if s[start]==s[end]:
                start=start-1
                end=end+1
            else:
                break
                
        start=start+1
        end=end-1
        
        if self.maxlen<end-start+1:
            self.start=start
            self.maxlen=end-start+1
    
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)==0:
            return s
        
        
        for i in range(len(s)):
            self.palindromesub(i,i,s)
            self.palindromesub(i,i+1,s)
            
        return s[self.start:self.start+self.maxlen]
            
 #DP      
 #Time comp --> o(n2)
#space comp --> o(n2)
 
 class Solution:
    
    def __init__(self):
        self.maxlen=0
        self.start=0
    
    def longestPalindrome(self, s: str) -> str:

        if len(s)==0:
            return ""
        
        count=0
        
        dp=[[False for i in range(len(s))]for j in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i]=True
            self.maxlen=1
            self.start=i
            
        for start in range(len(s)-1,-1,-1):
            for end in range(start+1,len(s)):
                
                if s[start]==s[end]:
                    
                    if end-start==1 or dp[start+1][end-1]:
                        dp[start][end]=True
                        if end-start+1>self.maxlen:
                            self.maxlen=end-start+1
                            self.start=start
                        
                        
        return s[self.start:self.start+self.maxlen]
        
        
        