class Twitter:

    def __init__(self):
        self.time=0
        self.followmap=defaultdict(set)
        self.tweetmap=defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]

        self.followmap[userId].add(userId)
        for followee in self.followmap[userId]:
            tweet=self.tweetmap[followee]
            if tweet:
                index=len(tweet)-1
                time,tweetid=tweet[index]

                heapq.heappush(heap,(-time,tweetid,followee,index-1))
        while heap and len(res)<10:
            negtime,tweetid,user,index=heapq.heappop(heap)
            res.append(tweetid)
            if index>=0:
                time,tweet=self.tweetmap[user][index]
                heapq.heappush(heap,(-time,tweet,user,index-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
