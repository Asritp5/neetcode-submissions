class Node:
    def __init__(self,key=-1,val=-1,prev=None,nxt=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.nxt=nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.myDict={}
        self.head=Node()
        self.tail=Node()
        self.head.nxt=self.tail
        self.tail.prev=self.head
        self.size=capacity

    def get(self, key: int) -> int:
        value=-1
        if key in self.myDict:
            value=self.myDict[key].val
            self.adjustNode(key)
        return value    

    def put(self, key: int, value: int) -> None:
        if key in self.myDict:
            self.myDict[key].val=value
            self.adjustNode(key)
        else:
            node=Node(key,value)
            self.myDict[key]=node
            if self.size>0:
                self.size-=1
            else:
                prev_node=self.tail.prev
                prev_node.prev.nxt=self.tail
                self.tail.prev=prev_node.prev
                del self.myDict[prev_node.key]

            node.nxt=self.head.nxt
            node.nxt.prev=node
            self.head.nxt=node
            node.prev=self.head

    def adjustNode(self,key):
        node=self.myDict[key]

        node.prev.nxt=node.nxt
        node.nxt.prev=node.prev

        node.nxt=self.head.nxt
        node.nxt.prev=node
        self.head.nxt=node
        node.prev=self.head

                


