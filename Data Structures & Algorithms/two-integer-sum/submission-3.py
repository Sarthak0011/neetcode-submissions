class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i in range(len(nums)):
            curr = nums[i]
            remaining = target - curr
            if remaining in mpp:
                return [mpp[remaining], i]
            mpp[curr] = i
        return [-1, -1]