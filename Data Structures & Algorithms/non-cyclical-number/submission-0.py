class Solution:
    def myFun(self,n,seen):
        if n==1:
            return True

        total=0
        while n:
            digit=n%10
            total+=digit**2
            n//=10
        
        if total in seen:
            return False

        seen.add(total)
        return self.myFun(total,seen)    

                
    def isHappy(self, n: int) -> bool:
        return self.myFun(n,set())