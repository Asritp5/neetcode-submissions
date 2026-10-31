class CountSquares:

    def __init__(self):
        self.seen=set()
        self.points=defaultdict(int)        

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])]+=1
        self.seen.add((point[0],point[1]))

    def count(self, point: List[int]) -> int:
        total=0

        for px,py in self.seen:
            if point[0]==px and point[1]==py:
                continue
            count=1
            if abs(point[0]-px)==abs(point[1]-py):
                count*=self.points[(px,py)]
                count*=self.points[(point[0],py)]
                count*=self.points[(px,point[1])]
                
                total+=count

        return total            
                
                

