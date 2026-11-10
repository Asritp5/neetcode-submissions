class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True

        myDict=defaultdict(list)
        res=[]
        initial=[-1,-1,-1]
        n=len(triplets)

        for i in range(n):
            if triplets[i][0]>target[0] or triplets[i][1]>target[1]\
            or triplets[i][2]>target[2]:
                continue
            initial[0]=max(initial[0],triplets[i][0])
            initial[1]=max(initial[1],triplets[i][1])
            initial[2]=max(initial[2],triplets[i][2])

            if initial[0]==target[0] and initial[1]==target[1] and \
            initial[2]==target[2]:
                return True
        return False        
