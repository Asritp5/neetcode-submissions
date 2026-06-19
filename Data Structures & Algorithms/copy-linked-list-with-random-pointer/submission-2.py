"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myDict={None:None,}

        temp=head
        while temp:
            if temp not in myDict:
                myDict[temp]=Node(temp.val)
            if temp.next not in myDict:
                myDict[temp.next]=Node(temp.next.val)
            if temp.random not in myDict:
                myDict[temp.random]=Node(temp.random.val)
            myDict[temp].next=myDict[temp.next]
            myDict[temp].random=myDict[temp.random]

            temp=temp.next
            
        return myDict[head]