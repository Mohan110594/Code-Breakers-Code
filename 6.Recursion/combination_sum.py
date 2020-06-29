#TIme comp -->
#space comp -->


class Solution(object):
    def __init__(self):
        self.out=[]
    
    def backtrack(self,candidates,index,target,list1,sum1):
        if sum1>target:
            return
        if sum1==target:
            self.out.append(list(list1))
            return
        
        for i in range(index,len(candidates)):
            list1.append(candidates[i])
            self.backtrack(candidates,i,target,list1,sum1+candidates[i])
            list1.pop()
            
        
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.backtrack(candidates,0,target,[],0)
        
        return self.out