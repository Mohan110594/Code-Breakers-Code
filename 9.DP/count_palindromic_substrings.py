#Time comp --> o(n2)
#space comp --> o(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        count=0
        for i in range(len(s)):
            
            for left,right in [(i,i),(i,i+1)]:
                while left>=0 and right<len(s):
                    if s[left]==s[right]:
                    
                        left=left-1
                        right=right+1
                    else:
                        
                        break
                    
                count+=(right-left)//2
        
        return count