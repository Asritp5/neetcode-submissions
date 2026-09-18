class Solution:
    def createAdjList(self,flights,n):
        adj=[[]for _ in range(n)]

        for u,v,w in flights:
            adj[u].append((v,w))

        return adj    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList=self.createAdjList(flights,n)
        queue=[]
        cost=[math.inf]*n
        cost[src]=0
        queue.append((0,0,src))

        while queue:
            stops,cur_cost,node=heapq.heappop(queue)

            if stops>k:
                continue

            for adj_node,cst in adjList[node]:
                if cost[adj_node]>cur_cost+cst:
                    cost[adj_node]=cur_cost+cst
                    heapq.heappush(queue,(stops+1,cost[adj_node],adj_node))

        return cost[dst] if cost[dst]!=math.inf else -1            

