#Time --> o(n**2)
#space --> o(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for left,right in [(i,i),(i,i+1)]:
                # print(left,right)
                while left>=0 and right<len(s):
                    if s[left]==s[right]:
                        left=left-1
                        right=right+1
                    else:
                        break
            
                count+=(right-left)//2
                # print(left,right,count)
        return count
        
        
