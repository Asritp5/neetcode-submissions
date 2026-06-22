# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=tail=ListNode()
        carry=0

        while l1 and l2:
            total=l1.val+l2.val+carry
            carry=total//10
            total%=10

            l1.val=total
            tail.next=l1
            tail=tail.next
            l1=l1.next
            l2=l2.next

        temp= l1 or l2
        
        while temp:
            tail.next=temp
            tail=tail.next
            if not carry:
                return head.next

            total=temp.val+carry
            carry=total//10
            total=total%10 
            temp.val=total
            temp=temp.next

        if carry:
            tail.next=ListNode(1)
    
        return head.next



