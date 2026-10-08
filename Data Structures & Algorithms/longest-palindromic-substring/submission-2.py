class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start=0
        max_len=1

        for i in range(n):

            #odd palindrome
            left,right=i-1,i+1
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1

            if right-1-left >max_len:
                max_len=right-left-1
                start=left+1


            #even palindrome
            if i<n-1 and s[i]==s[i+1]:
                left,right=i,i+1
                while left>=0 and right<n and s[left]==s[right]:
                    left-=1
                    right+=1

                if right-1-left >max_len:
                    max_len=right-left-1
                    start=left+1

        return s[start:start+max_len]            
                