class Node:
    def __init__(self,key=0,value=0,next=None,prev=None):
        self.val=value
        self.key=key
        self.next=next
        self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):
        self.myDict={}
        self.cap=capacity
        self.count=0
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def adjust(self,key,value):
        node=self.myDict[key]
        node.prev.next=node.next
        node.next.prev=node.prev
        node.next=self.head.next
        node.prev=self.head
        node.next.prev=node
        self.head.next=node    
        node.val=value

    def get(self, key: int) -> int:
        if key in self.myDict:
            value=self.myDict[key].val        
            self.adjust(key,value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.myDict:
            self.adjust(key,value)
            return

        if self.cap<=self.count:
            node=self.tail.prev
            self.tail.prev=node.prev
            node.prev.next=self.tail
            del self.myDict[node.key]
        else:
            self.count += 1

        node=Node(key,value,self.head.next,self.head)
        self.myDict[key]=node
        self.head.next=node
        node.next.prev=node
