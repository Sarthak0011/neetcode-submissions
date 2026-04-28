class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mpp = {}

        for i in range(n):
            remaining = target - nums[i]
            if remaining in mpp:
                return [mpp[remaining], i]
            mpp[nums[i]] = i
        return [-1, -1]