class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)

        if m>n:
            return False
        
        c=Counter(s1)
        count=m
        left=0

        for right in range(n):
            c[s2[right]]-=1

            if c[s2[right]]<0:
                
                while c[s2[right]]<0:
                    c[s2[left]]+=1
                
                    if c[s2[left]]>0:
                        count+=1
                
                    left+=1
            else:
                
                count-=1

            if count==0:
                return True

        return False                                                            