# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp1,tmp2=l1,l2
        carry=0

        head=tail=ListNode()
        while tmp1 and tmp2:
            total=carry+tmp1.val+tmp2.val
            carry=total//10
            total=total%10

            tmp1.val=total
            tail.next=tmp1
            tail=tail.next
            tmp1=tmp1.next
            tmp2=tmp2.next

        if tmp1 or tmp2:
            tmp3=tmp1 or tmp2
    
            while tmp3:
                total=tmp3.val+carry
                carry=total//10
                total%=10

                tail.next=tmp3
                tmp3.val=total
                tail=tail.next
                tmp3=tmp3.next

                if not carry:
                    return head.next

        if carry:
            tail.next=ListNode(1)

        return head.next    


