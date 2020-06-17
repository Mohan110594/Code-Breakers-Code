#Time comp --> o(n)
#space comp --> o(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#1.find count of LLA and LLB.
#2.calculate the diff in the count of both the Linked lists.
#3.traverse by the diff amount on the linked list which is having greater length.
#4.then traverse both LLA and LLB till both of them reach at a intersection.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tempA=headA
        tempB=headB
        countA=0
        countB=0
        while tempA!=None:
            countA=countA+1
            tempA=tempA.next
            
        while tempB!=None:
            countB=countB+1
            tempB=tempB.next
        flag=0
        if countA>countB:
            diff=countA-countB
            flag=1
        else:
            diff=countB-countA
        if flag==1:
            while diff>0:
                headA=headA.next
                diff=diff-1
        else:
            while diff>0:
                headB=headB.next
                diff=diff-1
        
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA
        
        