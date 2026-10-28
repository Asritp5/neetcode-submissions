class Solution:
    def checkValidString(self, s: str) -> bool:
        min_close=max_close=0

        for ch in s:
            
            if ch=="(":
                min_close+=1
                max_close+=1
            elif ch==")":
                min_close-=1
                max_close-=1
            else:
                min_close-=1
                max_close+=1

            min_close=max(0,min_close)
            if max_close<0:
                return False

        return min_close==0                     
