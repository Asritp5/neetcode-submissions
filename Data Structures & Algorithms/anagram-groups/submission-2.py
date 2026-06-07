class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict={}
        
        result=[]
        for string in strs:
            freq=[0]*26

            for ch in string:
                freq[ord(ch)-ord("a")]+=1
            
            temp = tuple(freq)
            if temp in myDict:
                myDict[temp].append(string)
            else:
                res=[string,]
                myDict[temp]=res
                result.append(res)

        return result            