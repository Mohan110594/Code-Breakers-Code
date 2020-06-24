#Time comp --> o(n)
#space comp --> o(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts=[0 for i in range(26)]
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            counts[ord(s[i])-ord('a')]+=1
            counts[ord(t[i])-ord('a')]-=1
            
        for val in counts:
            if val!=0:
                return False
        return True