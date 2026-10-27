class Twitter:

    def __init__(self):
        self.posts=defaultdict(list)
        self.follower=defaultdict(list)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time,tweetId))    
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        
        for follower in self.follower[userId]:
            heap.extend(self.posts[follower][-10:])

        heap.extend(self.posts[userId][-10:])
        
        heapq.heapify(heap)

        feed=[]
        count=0
        while heap and count<10:
            _,tweet=heapq.heappop(heap)
            feed.append(tweet)
            count+=1

        return feed    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follower[followerId]:
            self.follower[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)

