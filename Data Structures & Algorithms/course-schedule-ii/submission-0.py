class Solution:
    def createAdjList(self,pre,n):
        adj=[[]for _ in range(n)]
        indegree=[0]*n
        for v,u in pre:
            adj[u].append(v)
            indegree[v]+=1
        return adj,indegree    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj,ind=self.createAdjList(prerequisites,numCourses)
        count=numCourses
        queue=deque()
        
        for i in range(numCourses):
            if ind[i]==0:
                queue.append(i)
                count-=1

        res=[]
        while queue:
            node=queue.popleft()        

            res.append(node)

            for adj_node in adj[node]:
                ind[adj_node]-=1
                if ind[adj_node]==0:
                    queue.append(adj_node)
                    count-=1

        if count==0:
            return res
        return []                
