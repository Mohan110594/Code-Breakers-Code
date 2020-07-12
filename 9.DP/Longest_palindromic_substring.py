#Expand around the center

#Time comp --> o(n2)
#space comp --> o(n2)

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
            
        
        
        