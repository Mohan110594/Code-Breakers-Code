#Time --> o(nk)
#space --> o(nk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        nums=[2,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101]
        d=dict()
        for val in strs:
            mul=1
            for value in val:
                mul=mul*nums[ord(value)-ord('a')]
            if mul not in d:
                d[mul]=[val]
            else:
                d[mul].append(val)
        out=[]
        for values in d.values():
            out.append(values)
        return out