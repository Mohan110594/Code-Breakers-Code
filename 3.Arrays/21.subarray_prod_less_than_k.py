#Time comp --> o(n)
#space comp --> o(1)

1.Calculate cumulative product at every index.
2.when the cumulative product is greater than a given k value then we reduce it to the values less than k.

consider the example [10,5,2,6] and k=100
     index=-1,i=0     10         10<100 --> out=0-(-1)=1  for the set [10]
              i=1        50       50<100 --> out=1+1-(-1)=3 which is for the sets [10],[5],[10,5]

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        rmul=1
        index=-1
        out=0
        if k<=1:
            return 0
        for i in range(len(nums)):
            rmul=rmul*nums[i]
            
            while rmul>=k:
                index=index+1
                rmul=rmul/nums[index]
            
            out=out+i-index
        
        return out