#Time comp --> o(nlog k)
#space comp --> o(k)

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h=[]
        
        for val in nums:
            if len(h)<k:
                heapq.heappush(h,val)
            else:
                if h[0]<val:
                    heapq.heappop(h)
                    heapq.heappush(h,val)
        return h[0]