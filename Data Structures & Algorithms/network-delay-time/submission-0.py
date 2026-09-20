class Solution:
    def createAdjList(self,times,n):
        adj=[[]for _ in range(n+1)]

        for u,v,t in times:
            adj[u].append((v,t))

        return adj    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList=self.createAdjList(times,n)
        vis=[math.inf]*(n+1)

        vis[0]=vis[k]=0
        heap=[(0,k)]

        while heap:
            cur_time,node=heapq.heappop(heap)

            if cur_time>vis[node]:
                continue

            for adj_node,adj_dist in adjList[node]:
                if vis[adj_node]>vis[node]+adj_dist:
                    vis[adj_node]=vis[node]+adj_dist
                    heapq.heappush(heap,(vis[adj_node],adj_node))

        if math.inf in vis:
            return -1

        return max(vis)                     