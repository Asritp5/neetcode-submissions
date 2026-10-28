class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        m,n=len(num1),len(num2)

        if m<n:
            m,n=n,m
            num1,num2=num2,num1

        zero=0
        res=''
        for i in range(n-1,-1,-1):
            prod=self.mul(num1,num2[i],zero)        
            res=self.add(res,prod)
            zero+=1

        return res    

    def mul(self,num1,digit,zero):
        digit,carry=ord(digit)-ord('0'),0
        i=len(num1)-1
        
        res=[]
        while i>=0 or carry:
            value=ord(num1[i])-ord('0') if i>=0 else 0
            ans=value*digit+carry
            res.append(str(ans%10))
            carry=ans//10
            i-=1

        res=res[::-1]
        return ''.join(res)+'0'*zero
    
    def add(self,num1,num2):
        if num1=='':
            return num2

        i,j,carry=len(num1)-1,len(num2)-1,0
        res=[]

        while i>=0 or j>=0 or carry:
            ans=ord(num1[i])-ord('0') if i>=0 else 0
            ans+=ord(num2[j])-ord('0') if j>=0 else 0
            ans+=carry
            res.append(str(ans%10))
            carry=ans//10
            i-=1
            j-=1
        res=res[::-1]
        return ''.join(res)