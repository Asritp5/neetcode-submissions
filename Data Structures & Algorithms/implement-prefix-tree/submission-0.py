class Node:
    def __init__(self):
        self.chars=[None]*26
        self.end=self.prefix=0

class PrefixTree:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        node=self.root
        
        for ch in word:
            index=ord(ch)-ord('a')
            if not node.chars[index]:
                node.chars[index]=Node()
            node=node.chars[index]
            node.prefix+=1
        node.end+=1        

    def search(self, word: str) -> bool:
        node=self.root
        
        for ch in word:
            index=ord(ch)-ord('a')
            if not node.chars[index]:
                return False
            node=node.chars[index]
            
        return node.end!=0
        
    def startsWith(self, word: str) -> bool:
        node=self.root
        
        for ch in word:
            index=ord(ch)-ord('a')
            if not node.chars[index]:
                return False
            node=node.chars[index]
            
        return node.prefix!=0
        
        