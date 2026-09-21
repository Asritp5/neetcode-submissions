class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList=[[]for _ in range(26)]
        indegree=[0]*26 
        seen=set(ord(ch)-ord('a') for w in words for ch in w)

        for i in range(len(words)-1):
                w1,w2=words[i],words[i+1]
                m,n=len(w1),len(w2)
                
                if m>n and w1[:n]==w2[:n]:
                    return ""

                for j in range(min(m,n)):
                    if w1[j]!=w2[j]:
                        adjList[ord(w1[j])-ord('a')].append(ord(w2[j])-ord('a'))
                        indegree[ord(w2[j])-ord('a')]+=1 
                        break
                

        queue=deque()
        for i in range(26):
            if indegree[i]==0 and i in seen:
                queue.append(i)
        
        res=[]
        while queue:
            alphabet=queue.popleft()
            res.append(chr(ord('a')+alphabet))

            for adj_node in adjList[alphabet]:
                indegree[adj_node]-=1
                if indegree[adj_node]==0:
                    queue.append(adj_node)        

        for i in range(26):
            if indegree[i]>0 and i in seen:
                return ""

        return "".join(res)                    