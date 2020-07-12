#Time comp --> o(n)
#space comp --> o(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        dp=[[0 for i in range(2)]for j in range(len(nums))]
        
        dp[0][1]=nums[0]
        
        for i  in range(1,len(nums)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            dp[i][1]=nums[i]+dp[i-1][0]
            
            
        # print(dp)
        return max(dp[len(dp)-1][0],dp[len(dp)-1][1])
    
    
        