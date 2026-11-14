class Solution:
    def myFun(self,dp,text1,text2,index1,index2):
        if index1==0 and index2==0:
            if text1[index1]==text2[index2]:
                return 1
            return 0
            
        if index1<0 or index2<0:
            return 0

        if dp[index1][index2]!=-1:
            return dp[index1][index2]

        val1=val2=val3=0
        if text1[index1]==text2[index2]:
            val1=self.myFun(dp,text1,text2,index1-1,index2-1)+1

        val2=self.myFun(dp,text1,text2,index1-1,index2)
        val3=self.myFun(dp,text1,text2,index1,index2-1)
        
        dp[index1][index2]=max(val1,val2,val3)
        return dp[index1][index2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[-1]*n for _ in range(m)]
        return self.myFun(dp,text1,text2,m-1,n-1)