class Solution:
    def myFun(self,temp,res,index,n,digits,myDict):
        if index>=n:
            res.append("".join(temp))
            return 

        for ch in myDict[digits[index]]:
            temp.append(ch)
            self.myFun(temp,res,index+1,n,digits,myDict)
            temp.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        myDict={"2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz",
        }

        res=[]
        n=len(digits)
        if n==0:
            return res
        self.myFun([],res,0,n,digits,myDict)
        return res