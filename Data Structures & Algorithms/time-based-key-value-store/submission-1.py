class TimeMap:

    def __init__(self):
        self.keyDict=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyDict[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        ans=-1

        arr=self.keyDict[key]
        low,high=0,len(arr)-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid][0]<=timestamp:
                ans=mid
                low=mid+1
            else:
                high=mid-1

        if ans==-1:
            return ""
        return arr[ans][1]

