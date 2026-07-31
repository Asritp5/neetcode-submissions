class Solution:
    def myFun(self,n):
        total=0
        while n:
            digit=n%10
            total+=digit**2
            n//=10
        
        return total    
               
    def isHappy(self, n: int) -> bool:
        slow,fast=n,self.myFun(n)
        power=dist=1

        while slow!=fast:
            if power==dist:
                slow=fast
                dist=0
                power+=1

            fast=self.myFun(fast)
            dist+=1

        return fast==1    
            