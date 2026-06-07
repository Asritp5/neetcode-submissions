class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict={}
        result=[]

        for string in strs:
            temp="".join(sorted(string))
            

            if temp in myDict:
                myDict[temp].append(string)
            else:
                res=[string,]
                myDict[temp]=res
                result.append(res)

        return result            