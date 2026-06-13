class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        freq = [[] for i in range(N+1)]

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for val, cnt in count.items():
            freq[cnt].append(val)
        
        i = N
        ans = []
        while i >= 0:
            while k > 0 and freq[i]:
                ans.append(freq[i].pop())
                k -= 1
            i -= 1
        return ans