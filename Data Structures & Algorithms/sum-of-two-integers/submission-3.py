class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        carry=0
        total=0
        for i in range(32):
            bit1=a&1
            bit2=b&1

            a=a>>1
            b=b>>1

            bit=carry^bit1^bit2
            carry=(carry+bit1+bit2)>=2
            
            if bit:
                total=total|1<<i
            
        if total>2147483647:
            return -(total^0xFFFFFFFF)-1

        return total            
