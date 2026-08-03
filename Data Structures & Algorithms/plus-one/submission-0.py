class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index=len(digits)-1
        carry=1
        
        while carry!=0 and index>=0:
            digits[index]+=carry
            carry=digits[index]//10
            digits[index]%=10
            
            index-=1

        if carry:
            digits.insert(0,1)

        return digits        

        