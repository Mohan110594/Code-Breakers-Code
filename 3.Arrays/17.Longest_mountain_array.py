#Time comp --> o(n)
#space comp --> o(1)
using Two pointers:
1.Traverse through the given input.check where there is peak. i.e when A[i]>A[i-1] and A[i]>A[i+1].
2.Then take two pointers one on the left side and the other on the right side of the peak element.
3.Expand the given window  using left and right pointers and as long as the condition applies .

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        maxi=0
        n=len(A)
        i=1
        while i<len(A)-1:
            if A[i-1]<A[i] and A[i]>A[i+1]:
                left=i-2
                right=i+2
                while left>-1 and A[left]<A[left+1]:
                    left=left-1
                while right<n and A[right-1]>A[right]:
                    right=right+1
                maxi=max(maxi,right-left-1)
                i=right
            else:
                i=i+1
                
        return maxi
            
            

DP Solution:
1.create a left array which has the count of elements less than to the left of the current element in the given array.
2. Create a right array which has the count of elements less than to the right side of the current element in the given array.
3.Take the indices which are having both left and right side elements to form a mountain and calculate the maximum at each and every index.

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        left=[0 for i in range(len(A))]
        right=[0 for i in range(len(A))]
        
        maxi=0
        
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                left[i]=left[i-1]+1
            
            if A[len(A)-i-1]>A[len(A)-i]:
                right[len(A)-i-1]=right[len(A)-i]+1
        
        # print(left,right)
        for i  in range(len(left)):
            if left[i]>0 and right[i]>0:
                maxi=max(maxi,1+left[i]+right[i])
        
        return maxi
            
            
                
                         
            