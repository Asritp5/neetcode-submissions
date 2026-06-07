class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        first,last=0,len(s)-1

        
        while first<last:

            while first<last and not ("a"<=s[first]<="z" or "0"<=s[first]<="9"):
                first+=1

            if first>=last:
                return True

            while first<last and not ("a"<=s[last]<="z" or "0"<=s[last]<="9"):
                last-=1

            if first>=last:
                return True

            if s[first]==s[last]:
                last-=1
                first+=1
            else:
                return False        
        return True