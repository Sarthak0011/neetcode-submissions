class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followings[userId].add(userId)
        maxHeap = []
        for followeeId in self.followings[userId]:
            tweets = self.posts[followeeId]
            if not tweets: continue

            latestTweetIndex = len(tweets) - 1

            tweetTime, tweet = tweets[latestTweetIndex]
            maxHeap.append([
                tweetTime, 
                tweet, 
                followeeId, 
                latestTweetIndex-1
            ])
        
        heapq.heapify(maxHeap)

        feed = []
        while maxHeap and len(feed) < 10:
            tweetTime, tweet, followeeId, nextTweetIndex = heapq.heappop(maxHeap)
            feed.append(tweet)

            if nextTweetIndex >= 0:
                nextTweetTime, nextTweet = self.posts[followeeId][nextTweetIndex]
                heapq.heappush(maxHeap, [
                    nextTweetTime,
                    nextTweet,
                    followeeId,
                    nextTweetIndex - 1
                ])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)
