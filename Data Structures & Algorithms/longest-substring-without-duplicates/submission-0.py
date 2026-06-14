class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=Counter()

        left=max_len=0
        n=len(s)

        for right in range(n):
            c[s[right]]+=1
            
            while c[s[right]]!=1 and left<=right:
                c[s[left]]-=1
                left+=1

            max_len=max(max_len,right-left+1)

        return max_len        
                