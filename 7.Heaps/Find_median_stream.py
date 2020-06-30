
import heapq
class MedianFinder:

    def __init__(self):
        # lowerhalf to maintain the least  values in the array below the median(max heap)
        self.lowerhalf=[]
        # higherhalf to maintain the values in the array which are greater than the median(min heap)
        self.higherhalf=[]

    def addNum(self, num: int) -> None:
        #Time --> o(log n)
        #space --> o(n)
        # we add the incoming element into the lowerhalf
        heapq.heappush(self.lowerhalf,num)
        # To balance the element addition in lowerhalf we add the max value from the lowerhalf to the higherhalf
        val=heapq.heappop(self.lowerhalf)
        heapq.heappush(self.higherhalf,-1*val)
        
        # length of lowerhalf can be equal to or one greater than the length of the higherhalf
        # if it is greater we pop the min element from the higher half to the lower half
        if len(self.higherhalf)>len(self.lowerhalf):
            value=heapq.heappop(self.higherhalf)
            heapq.heappush(self.lowerhalf,-1*value)

    def findMedian(self) -> float:
    #Time --> o(1)
    #space --> o(1)
        # if lengths of both the halves are equal then it means it has even number of elements so we take avg of mid and mid+1 elements
        if len(self.lowerhalf)==len(self.higherhalf):
            return ((self.lowerhalf[0]-self.higherhalf[0])*0.5)
        else:
            # we return the extra element from the lowerhalf
            return (self.lowerhalf[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()