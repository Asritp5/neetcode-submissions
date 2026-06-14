class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=max_len=max_fr=0
        n=len(s)
        c=Counter()

        for right in range(n):
            c[s[right]]+=1
            max_fr=max(max_fr,c[s[right]])
            while right-left+1 - max_fr>k:
                c[s[left]]-=1
                left+=1

            max_len=max(max_len,right-left+1)

        return max_len    
