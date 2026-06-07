class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        first,last=0,len(s)-1
        while first<last:

            while first<last and not s[first].isalnum():
                first+=1

            if first>=last:
                return True

            while first<last and not s[last].isalnum():
                last-=1

            if first>=last:
                return True

            if s[first].lower()==s[last].lower():
                last-=1
                first+=1
            else:
                return False        
        return True