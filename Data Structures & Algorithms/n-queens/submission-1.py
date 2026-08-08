class Solution:
    def myFun(self,sol,index,n,pos,neg,col,res):
        if index>=n:
            res.append(sol[:])
            return 

        for i in range(n):
            if index+i not in pos and index-i not in neg and i not in col:
                pos.add(index+i)
                neg.add(index-i)
                col.add(i)
                sol[index]=i
                self.myFun(sol,index+1,n,pos,neg,col,res)
                pos.discard(index+i)
                neg.discard(index-i)
                col.discard(i)

                
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol=[0]*n
        result=[]
        self.myFun(sol,0,n,set(),set(),set(),result)

        answer=[]
        for res in result:
            answer.append(self.makeBoard(res,n))

        return answer

    def makeBoard(self,res,n):
        ans=[]
        for num in res:
            ans.append("."*num+"Q"+"."*(n-num-1))

        return ans            