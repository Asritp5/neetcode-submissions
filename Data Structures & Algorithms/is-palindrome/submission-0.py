class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        result=[]
        for ch in s:
            if "a"<=ch<="z" or "0"<=ch<="9":
                result.append(ch)

        myString="".join(result)

        first,last=0,len(myString)-1

        while first<last:
            if myString[first]!=myString[last]:
                return False

            first+=1
            last-=1

        return True                