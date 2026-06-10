class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        n3-> brute force 3 loops
        n2-> 2 loops + 1 dictionary
        nlogn + n2 -> sort and 3 pointers 
        """

        nums.sort()
            
        result=[]

        n=len(nums)
        
        for i in range(n):
            if nums[i]>0:
                continue
                
            if i>0 and nums[i]==nums[i-1]:
                continue

            j,k=i+1,n-1

            while j<k:
    
                if nums[i]+nums[j]+nums[k]==0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while j>i+1 and j<k and nums[j-1]==nums[j]:
                        j+=1

                    while k<n-1 and j<k and nums[k+1]==nums[k]:
                        k-=1

                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1

                else:
                    k-=1                    

        return result                


                