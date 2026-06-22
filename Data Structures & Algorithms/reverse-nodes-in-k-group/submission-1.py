# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head,stop,pre):
        cur=head
        prev=None
        while cur!=stop:
            tmp=cur.next
            cur.next=prev
            prev,cur=cur,tmp

        pre.next=prev
        return prev,head    

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        HEAD=ListNode(-1)
        start=stop=head
        pre=HEAD
        while True:
            count=0

            while stop and count<k:
                stop=stop.next
                count+=1

            if count==k:
                start,end=self.reverse(start,stop,pre)
                start=stop
                pre=end
            else:
                pre.next=start
                break

        return HEAD.next    