class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)

        vehicle=[]
        for i in range(n):
            time=(target-position[i])/speed[i]
            vehicle.append((position[i],speed[i],time))

        vehicle.sort(key=lambda x:x[0],reverse=True)

        stack=[]
        
        for i in range(n):
            if not stack or stack[-1]<vehicle[i][2]:
                stack.append(vehicle[i][2])

        return len(stack)        
        