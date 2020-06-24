#Time -->o(n**2)
#space --> o(1)
class Solution:
    def __init__(self):
        self.maxlen=0
        self.out=''
    def traversal(self,s,start,end):
        
        while start>=0 and end<len(s):
            
            if s[start]==s[end]:
                start=start-1
                end=end+1
            else:
                break
        start+=1
        end-=1
        # print(start,end)
        len1=end-start+1
        if len1>self.maxlen:
            self.out=s[start:end+1]
            self.maxlen=len1
        
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            
            self.traversal(s,i,i)
            self.traversal(s,i,i+1)
        return self.out
            