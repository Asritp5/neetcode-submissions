class Solution:
    def myFun(self,n):
        total=0
        while n:
            digit=n%10
            total+=digit**2
            n//=10
        
        return total    
               
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.myFun(n)

        while slow!=fast:
            slow=self.myFun(slow)
            fast=self.myFun(self.myFun(fast))

        return fast==1    
            