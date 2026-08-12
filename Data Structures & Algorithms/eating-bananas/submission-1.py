class Solution:
    def check(self,piles,mid,h):
        total=0
        for p in piles:
            total+=p//mid
            if p%mid:
                total+=1
            if total>h:
                return -1
        return 1        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)

        ans=-1
        while low<=high:
            mid=(low+high)//2

            value=self.check(piles,mid,h)
            if value==1:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans
