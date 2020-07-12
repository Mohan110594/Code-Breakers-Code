# memoization
# Time comp --> o(m*n)
# space comp --> o(m*n)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1=sum(nums)
        
        if sum1%2!=0:
            return False
        
        dp=[[-1 for i in range((sum1//2)+1)]for j in range(len(nums))]
        
        return self.knapsack(nums,sum1//2,0,dp)
    
    
    def knapsack(self,nums,sum1,index,dp):
        
        if sum1==0:
            return 1
        
        if index>=len(nums):
            return 0
        
        
        if dp[index][sum1]==-1:
            if nums[index]<=sum1:
                if self.knapsack(nums,sum1-nums[index],index+1,dp)==1:
                    dp[index][sum1]=1
                    return 1
            
        dp[index][sum1]=self.knapsack(nums,sum1,index+1,dp)
        
        return dp[index][sum1]
        
        
# DP
# Time comp --> o(mn)
# space comp --> o(mn)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if len(nums)<=1:
            return False
        
        sum1=sum(nums)
        
        if sum1%2!=0:
            return False
        
        half=sum1//2
        
        dp=[[False for i in range(half+1)]for j in range(len(nums))]
        
        
        for i in range(len(dp)):
            dp[i][0]=True
            
        # This base case is  tricky
        for j in range(1,len(dp[0])):
            dp[0][j]= nums[0]==j
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                # If the prev row is True then only we take the value from the prev row else we take False from the prev row for all the values j<nums[i]
                if dp[i-1][j]:
                    dp[i][j]=dp[i-1][j]
                    
                
                elif j >= nums[i]:
                    dp[i][j]=dp[i-1][j-nums[i]]
                    
        # print(dp)
                    
        return dp[len(dp)-1][len(dp[0])-1]