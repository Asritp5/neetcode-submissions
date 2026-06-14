class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDict={}

        left=max_len=0
        n=len(s)

        for right in range(n):
            if s[right] in myDict:
                left=max(left,myDict[s[right]]+1)
            
            myDict[s[right]]=right
            max_len=max(max_len,right-left+1)

        return max_len        
                