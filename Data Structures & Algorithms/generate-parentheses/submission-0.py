class Solution:
    def myFun(self,res,temp,open_br,closed_br,n):
        if open_br==n and closed_br==n:
            res.append("".join(temp))
            return 

        if open_br-closed_br>0:
            temp.append(")")
            self.myFun(res,temp,open_br,closed_br+1,n)
            temp.pop()

        if open_br<n:
            temp.append("(")
            self.myFun(res,temp,open_br+1,closed_br,n)
            temp.pop()

                    
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.myFun(res,[],0,0,n)
        return res