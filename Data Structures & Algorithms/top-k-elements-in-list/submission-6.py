class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        mpp = {}
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1

        bucket = [[] for i in range(n+1)]
        for key, value in mpp.items():
            bucket[value].append(key)

        ans = []
        i = n
        while (i > 0 and k > 0):
            temp = bucket[i]
            for num in temp:
                ans.append(num)
                k -= 1
                if k == 0:
                    break
            i -= 1
        
        return ans
