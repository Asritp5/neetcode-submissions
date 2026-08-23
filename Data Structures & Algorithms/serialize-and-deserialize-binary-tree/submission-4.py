# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue=deque([root])
        res=[]
        while queue:
            node=queue.popleft()
            
            if node:
                res.append(str(node.val)+",")
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("None,")

        return "".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr=data.split(",")
        arr.pop()
        
        n=len(arr)
        
        if n==0:
            return None
          
        myDict={} 
        for i in range(n):
            if arr[i]!="None":
                myDict[i]=TreeNode(int(arr[i]))
            else:
                myDict[i]=None
        
        index=1
        for i in range(n):
            if  myDict[i]:
                if index<n:
                    myDict[i].left=myDict[index]
                index+=1
                if index<n:
                    myDict[i].right=myDict[index]
                index+=1            
        return myDict[0]        