# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0

        temp=head
        while temp:
            temp=temp.next
            count+=1

        target=count-n
        if target==0:
            return head.next
        
        count=0
        temp=head
        while temp:
            count+=1
            if count==target:
                temp.next=temp.next.next
                break
            temp=temp.next

        return head    
    