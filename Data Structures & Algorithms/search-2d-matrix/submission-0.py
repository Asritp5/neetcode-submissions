class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])

        low,high=0,m-1

        ans=-1
        while low<=high:
            mid=(low+high)//2

            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                ans=mid
                low=mid+1
            else:
                high=mid-1

        if ans==-1:
            return False

        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2

            if matrix[ans][mid]==target:
                return True
            elif matrix[ans][mid]<target:
                low=mid+1
            else:
                high=mid-1

        return False
            
