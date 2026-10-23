class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n=len(s),len(t)

        if n>m:
            return ""

        start=end=-1
        char_set=set(t)
        char_count=len(char_set)
        left,min_len=0,math.inf
        target=Counter(t)
        
        for right in range(m):
            target[s[right]]-=1
            if target[s[right]]==0:
                char_count-=1

            while left<m and target[s[left]]<0:
                target[s[left]]+=1
                if target[s[left]]>0:
                    char_count+=1
                left+=1

            if char_count==0 and min_len>right-left+1:
                min_len=right-left+1
                start,end=left,right   

        return s[start:end+1] if min_len!=math.inf else ""                         
                            
