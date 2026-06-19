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
            myDict[temp]=Node(temp.val)
            temp=temp.next

        temp=head
        while temp:
            node=myDict[temp]
            node.next,node.random=myDict[temp.next],myDict[temp.random]
            temp=temp.next
            
        return myDict[head]