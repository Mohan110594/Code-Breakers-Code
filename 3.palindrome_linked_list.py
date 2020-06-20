#Time complexity --> o(n)
#space complexity --> o(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#1.Traverse to the id of linked list.
#2.reverse the second half of the LL.
#3.compare the values of the first and second half of the linked list.



class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return True
        slow=head
        fast=head
        # traverse to the mid of the LL
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        # reverse the second half of the LL
        
        prev=None
        curr=slow.next  
        while curr!=None:
            
            next1=curr.next
            curr.next=prev
            prev=curr
            curr=next1
        
        # we have to compare the values from first and last values
        
        temp=head
        while prev!=None:
            
            if prev.val!=temp.val:
                return False
            temp=temp.next
            prev=prev.next
        return True
            