
using a set:
#Time comp --> o(n)
#space comp --> o(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        start=0
        end=0
        values=set()
        maxi=float('-inf')
        while end<len(s):
            if s[end] not in values:
                values.add(s[end])
            else:
                while s[end] in values:
                    values.remove(s[start])
                    start+=1
                continue
            
            maxi=max(maxi,end-start+1)
            end+=1
        return maxi
        
        
using a Dictionary:

Time comp --> o(n)
space comp --> o(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index=0
        i=0
        values=dict()
        maxi=0
        while i<len(s):
            # print(values)
            if s[i] not in values:
                values[s[i]]=i
            else:
                index=values[s[i]]+1
                i=index
                values=dict()
                continue
            maxi=max(maxi,i-index+1)
            i=i+1
        
        return maxi