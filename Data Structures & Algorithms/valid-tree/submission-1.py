class DisjointSet:
    def __init__(self,n):
        self.parent=[-1]*(n)

    def find(self,x):
        if self.parent[x]<0:
            return x

        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        par_x,par_y=self.find(x),self.find(y)

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)<n-1:
            return False
            
        DS=DisjointSet(n)

        for u,v in edges:
            if DS.union(u,v)==-1:
                return False
        
        return True        