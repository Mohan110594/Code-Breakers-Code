#Time complexity --> o(n)
#space complexity--> o(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=head
        slow=head
        while n>0:
            fast=fast.next
            n=n-1
        #when there is only one element in LL and that needs to be deleted then the below case
        if fast==None:
            return head.next
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head