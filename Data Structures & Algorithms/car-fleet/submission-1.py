class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)

        vehicle=[]
        for i in range(n):
            time=(target-position[i])/speed[i]
            vehicle.append((position[i],speed[i],time))

        vehicle.sort(key=lambda x:x[0],reverse=True)

        stack=[]
        fleets,cur_time=1,vehicle[0][2]
        
        for i in range(1,n):
            if cur_time<vehicle[i][2]:
                fleets+=1
                cur_time=vehicle[i][2]

        return fleets        
        