class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("inf")
        currSum = 0

        n = len(nums)
        i, j = 0, 0
        while i < n and j < n:
            currSum += nums[j]
            j += 1
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                i = j
                currSum = 0
        return maxSum