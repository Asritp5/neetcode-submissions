class DisjointSet:
    def __init__(self,n):
        self.parent=[-1]*(n+1)

    def find(self,node):
        if self.parent[node]<0:
            return node

        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]    

    def union(self,node1,node2):
        par_x,par_y=self.find(node1),self.find(node2)

        if par_x==par_y:
            return -1

        if self.parent[par_x]<=self.parent[par_y]:
            self.parent[par_x]+=self.parent[par_y]
            self.parent[par_y]=par_x
        else:
            self.parent[par_y]+=self.parent[par_x]
            self.parent[par_x]=par_y

        return 1    


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        Ds=DisjointSet(n)

        for u,v in edges:
            if Ds.union(u,v)==-1:
                return [u,v]
                