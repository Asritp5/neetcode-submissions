# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head,stop):
        prev=None
        cur=head

        while cur!=stop:
            tmp=cur.next
            cur.next=prev
            prev,cur=cur,tmp

        return prev,head    

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        myPtr=[]
        start=stop=head
        while True:
            count=0

            while stop and count<k:
                stop=stop.next
                count+=1

            if count==k:
                start,end=self.reverse(start,stop)
                myPtr.append([start,end])
                start=stop
            else:
                myPtr.append([start,None])
                break
                
        n=len(myPtr)
        for i in range(n-1):
            myPtr[i][1].next=myPtr[i+1][0]

        return myPtr[0][0]    