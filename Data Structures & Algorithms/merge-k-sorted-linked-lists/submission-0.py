# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel=tail=ListNode()

        n=len(lists)
        while True:
            min_val=math.inf
            min_index=-1
            flag=False
            for i in range(n):
                if lists[i] and lists[i].val<min_val:
                    flag=True
                    min_val=lists[i].val
                    min_index=i

            if not flag:
                return sentinel.next

            tail.next=lists[min_index]
            tail=tail.next 
            lists[min_index]=lists[min_index].next
