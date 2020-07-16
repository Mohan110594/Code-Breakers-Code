#Binary search
#Time comp --> o(nlogn)
#space comp --> o(n)
class Solution(object):
    def binarysearch(self,out,ele):
        low=0
        high=len(out)-1
        
        while low<high:
            mid=low+((high-low)//2)
            
            if ele>out[mid]:
                low=mid+1
                
            else:
                
                high=mid
                
        return low
    
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            
            return 0
        
        out=[nums[0]]
        
        for i in range(1,len(nums)):
            if nums[i]>out[-1]:
                out.append(nums[i])
                
            else:
                
                index=self.binarysearch(out,nums[i])
                out[index]=nums[i]
                
        return len(out)
        
 #DP
 #Time comp --> o(n2)
 #space comp --> o(n)
 
 class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        dp=[1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
                              
        return max(dp)
        