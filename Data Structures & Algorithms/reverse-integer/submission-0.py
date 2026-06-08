class Solution:
    def reverse(self, x: int) -> int:
        total=0

        flag=False
        if x<0:
            flag=True
            x=abs(x)
        
        while x:
            total=total*10+x%10
            x=x//10

        if total<-2**31 or total>2**31-1:
            return 0

        return total if not flag else -total        