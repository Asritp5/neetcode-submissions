class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        
        if m>n:
            return False
        
        c=[0]*26
        
        for i in range(m):
            index=ord(s1[i])-ord('a')
            c[index]+=1

        count=m
        left=0

        for right in range(n):
            index=ord(s2[right])-ord('a')
            c[index]-=1

            if c[index]<0:
                
                while c[index]<0:
                    c[ord(s2[left])-ord('a')]+=1
                
                    if c[ord(s2[left])-ord('a')]>0:
                        count+=1
                
                    left+=1
            else:
                
                count-=1

            if count==0:
                return True

        return False                                                            