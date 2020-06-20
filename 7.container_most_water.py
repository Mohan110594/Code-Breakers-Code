#Time comp-->  o(n)
#space comp--> o(1)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        low=0
        high=len(height)-1
        maxi=float('-inf')
        while low<high:
            # print(maxi)
            breadth=min(height[low],height[high])
            length=high-low
            maxi=max(maxi,length*breadth)
            if height[low]<height[high]:
                low=low+1
            else:
                high=high-1
        return maxi