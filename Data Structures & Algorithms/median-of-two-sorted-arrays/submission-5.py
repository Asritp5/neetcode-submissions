class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        if m==0:
            if n%2:
                return float(nums2[n//2])
            return (nums2[n//2-1]+nums2[n//2])/2    
        elif n==0:
            if m%2:
                return float(nums1[m//2])
            return (nums1[m//2-1]+nums1[m//2])/2    
        
        if m>n:
            m,n=n,m
            nums1,nums2=nums2,nums1

        low,high=0,m
        mid_point=(m+n+1)//2

        while low<=high:
            mid=(low+high)//2

            value11,value12=-math.inf,math.inf
            if mid-1>=0:
                value11=nums1[mid-1]
            if mid<m:
                value12=nums1[mid]
            
            index2=mid_point-mid
            value21,value22=-math.inf,math.inf
            if index2-1>=0:
                value21=nums2[index2-1]
            if index2<n:
                value22=nums2[index2]
            
            if value11>value22:
                high=mid-1
            elif value21>value12:
                low=mid+1
            else:
                if (m+n)%2:
                    return max(value11,value21)
                return (max(value11,value21)+min(value12,value22))/2


            