# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        temp=slow.next
        slow.next=None
        prev=None       
        while temp:
            tp=temp.next
            temp.next=prev
            prev,temp=temp,tp

        
        sentinel=tail=ListNode()
        temp1,temp2=head,prev

        while temp1 and temp2:
            tail.next=temp1
            temp1=temp1.next
            tail=tail.next
            tail.next=temp2
            temp2=temp2.next
            tail=tail.next

        if temp1:
            tail.next=temp1
        elif temp2:
            tail.next=temp2 

        

