class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = {}
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1
        
        import heapq
        pq = []

        for num, freq in mpp.items():
            if len(pq) >= k:
                top_freq, top_num = pq[0]
                if freq > top_freq:
                    heapq.heappop(pq)
                    heapq.heappush(pq, (freq, num))
            else:
                heapq.heappush(pq, (freq, num))

        index = len(pq) - 1
        ans = [0] * len(pq)
        while pq:
            freq, num = heapq.heappop(pq)
            ans[index] = num
            index -= 1
        
        return ans

