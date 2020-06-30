#Time comp --> o(n logk)
#space comp --> o(k)
import math
import heapq
class Solution(object):
    def find_dist(self,val):
        return math.sqrt(pow(val[0],2)+pow(val[1],2))
    
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        out=[]
        result=[]
        for val in points:
            if len(out)<K:
                heapq.heappush(out,(-1*self.find_dist(val),val))
            else:
                distance=self.find_dist(val)
                if distance<-1*(out[0][0]):
                    heapq.heappop(out)
                    heapq.heappush(out,(-1*distance,val))
                    
        while len(out)>0:
            result.append(heapq.heappop(out)[1])
        
        return result
                    
        