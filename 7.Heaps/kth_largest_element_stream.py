import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time comp --> o(n logk)
        # space comp -->o(k)
        self.list1=[]
        self.k=k
        for val in nums:
            if len(self.list1)<k:
                heapq.heappush(self.list1,val)
            else:
                if val>self.list1[0]:
                    heapq.heappop(self.list1)
                    heapq.heappush(self.list1,val)

    def add(self, val: int) -> int:
        # Time comp --> o(log k)
        # space comp -->o(1)
        if len(self.list1)<self.k:
            heapq.heappush(self.list1,val)
        else:
            if val>self.list1[0]:
                heapq.heappop(self.list1)
                heapq.heappush(self.list1,val)
        return self.list1[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)