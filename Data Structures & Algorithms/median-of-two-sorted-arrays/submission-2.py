class Solution:
    
    def find_min(self,nums1,nums2,ptr,m,n):
            i,j=ptr[0],ptr[1]
            if i<m and j<n:
                if nums1[i]<nums2[j]:
                    result=nums1[i]
                    ptr[0]+=1        
                else:
                    result=nums2[j]
                    ptr[1]+=1

            elif i<m:
                result=nums1[i]
                ptr[0]+=1        
                
            else:
                result=nums2[j]
                ptr[1]+=1        
                
            return result    

    def return_result(self,nums1,nums2,ptr,m,n):
            i,j=ptr[0],ptr[1]        
            value1=self.find_min(nums1,nums2,ptr,m,n)                        
            even_flag=False
            if (m+n)%2==0:
                even_flag=True
            if even_flag:
                value2=self.find_min(nums1,nums2,ptr,m,n)                    
                return (value1+value2)/2
            else:
                return value1
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        m,n=len(nums1),len(nums2)

        i=j=count=0
        even_flag=False

        if (m+n)%2:
            mid=(m+n)//2
        else:
            even_flag=True
            mid=(m+n)//2-1    

        while i<m and j<n:
            if count==mid:
                return self.return_result(nums1,nums2,[i,j],m,n)        
            
            if nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
            count+=1
                    
        while i<m:
            if count==mid:
                return self.return_result(nums1,nums2,[i,j],m,n)        
            i+=1
            count+=1

        while j<n:
            if count==mid:
                return self.return_result(nums1,nums2,[i,j],m,n)        
            j+=1
            count+=1
                