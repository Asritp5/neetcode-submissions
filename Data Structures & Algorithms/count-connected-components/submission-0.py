class Solution:
    def createAdjList(self,n,edges):
        adj=[[]for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj 

    def bfs(self,node,vis,adjList):
        queue=deque([node,])
        vis[node]=True

        while queue:
            cur_node=queue.popleft()
            for adj_node in adjList[cur_node]:
                if not vis[adj_node]:
                    vis[adj_node]=True
                    queue.append(adj_node)
                    
        return 

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList=self.createAdjList(n,edges)
        vis=[False]*n
        count=0
        for i in range(n):
            if not vis[i]:
                self.bfs(i,vis,adjList)
                count+=1
        return count        