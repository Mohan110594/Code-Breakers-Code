#Time comp -->o(m+n)
#space comp -->o(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return nums1
        
        i=m-1
        j=n-1
        index=m+n-1
        while i>=0 and j>=0:
            if nums2[j]>nums1[i]:
                nums1[index]=nums2[j]
                j=j-1
                
            else:
                nums1[index]=nums1[i]
                i=i-1
            index=index-1
            # print(nums1)
        while j>=0:
            nums1[index]=nums2[j]
            j=j-1
            index=index-1
        return nums1