class Solution:
    def adjList(self,preq,n):
        adj=[[]for _ in range(n)]
        ind=[0]*n

        for v,u in preq:
            adj[u].append(v)
            ind[v]+=1

        return adj,ind    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj,indegree=self.adjList(prerequisites,numCourses)
        count=numCourses

        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
                count-=1

        while queue:
            node=queue.popleft()

            for adj_node in adj[node]:
                indegree[adj_node]-=1
                if indegree[adj_node]==0:
                    queue.append(adj_node)
                    count-=1

        return count==0                     