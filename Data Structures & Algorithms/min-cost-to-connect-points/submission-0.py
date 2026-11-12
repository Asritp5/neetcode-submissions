class DisjointSet:
    def __init__(self,n):
        self.parent=[-1]*n
    
    def find(self,x):
        if self.parent[x]<0:
            return x
        x=self.find(self.parent[x])
        return x
    
    def union(self,x,y):
        par_x,par_y=self.find(x),self.find(y)

        if par_x==par_y:
            return -1

        if self.parent[par_x]<self.parent[par_y]:
            self.parent[par_x]+=self.parent[par_y]
            self.parent[par_y]=par_x
        else:
            self.parent[par_y]+=self.parent[par_x]
            self.parent[par_x]=par_y

        return 1     

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n==1:
            return 0
            
        ds=DisjointSet(n)
        
        i=0
        myDict={}
        for px,py in points:
            myDict[(px,py)]=i
            i+=1 
        
        heap=[]
        for i in range(n):
            for j in range(i+1,n):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])    
                heap.append((dist,points[i],points[j]))

        heap.sort(key=lambda x:x[0])

        total=count=0
        for d,p1,p2 in heap:
            x1,y1=(p1[0],p1[1]),(p2[0],p2[1])
            id1,id2=myDict[x1],myDict[y1]
            if ds.union(id1,id2)!=-1:
                total+=d
                count+=1

                if count>=n-1:
                    return total
        return total            