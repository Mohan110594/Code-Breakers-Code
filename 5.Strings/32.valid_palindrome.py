Two pointers:
#Time comp --> o(n)
#space comp --> o(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low=0
        high=len(s)-1
        while low<high:
            while low<high and not s[low].isalnum():
                low+=1
            
            while low<high and not s[high].isalnum():
                high-=1
            # print(s[low],s[high])
            if low<high and s[low].lower()!=s[high].lower():
                return False
            
            low+=1
            high-=1
            
        return True
        
        
using extra space:

#Time comp --> o(n)
#space comp --> o(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        out=''
        for val in s:
            if val.isalpha():
                out=out+val.lower()
            elif val.isdigit():
                out=out+str(val)

        return out==out[::-1]