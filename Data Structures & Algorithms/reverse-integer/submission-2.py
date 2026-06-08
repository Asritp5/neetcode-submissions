class Solution:
    def reverse(self, x: int) -> int:
        total=0
        a,b=-2147483648,2147483647
        flag=False
        if x<0:
            flag=True
            x=abs(x)
        
        while x:
            total=total*10+x%10
            x=x//10

            if total<a or total>b:
                return 0

        return total if not flag else -total        