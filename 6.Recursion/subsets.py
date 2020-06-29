#TIme --> o(n*(2^n))
#space -->o(n*(2^n))

class Solution(object):
    def __init__(self):
        self.out=[]
        
    def backtrack(self,nums,index,list1):
        # print(list1)
        self.out.append(list(list1))
        
        for i in range(index,len(nums)):
            list1.append(nums[i])
            self.backtrack(nums,i+1,list1)
            list1.pop()
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.backtrack(nums,0,[])
        
        return self.out