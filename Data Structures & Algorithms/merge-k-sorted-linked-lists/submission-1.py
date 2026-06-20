# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel=tail=ListNode()

        heap=[]
        index=0
        for lst in lists:
            heap.append((lst.val,index,lst))
            index+=1

        heapq.heapify(heap)    
        while heap:
            _,_,node=heapq.heappop(heap)
            
            tail.next=node
            tail=tail.next 
            node=node.next
            if node:
                heapq.heappush(heap,(node.val,index,node))
                index+=1
        return sentinel.next