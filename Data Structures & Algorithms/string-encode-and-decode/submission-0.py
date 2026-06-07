class Solution:

    def encode(self, strs: List[str]) -> str:
        result=[]
        for string in strs:
            length=len(string)

            result.append(str(length))
            result.append("#")
            result.append(string)

        return "".join(result)
    def decode(self, s: str) -> List[str]:
        index=0
        result=[]
        
        n=len(s)

        while index<n:
            length=0
            while s[index]!="#":
                length=length*10+int(s[index])
                index+=1

            index+=1

            temp=[]    
            for i in range(length):
                temp.append(s[index])
                index+=1

            result.append("".join(temp))

        return result        