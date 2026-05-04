class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = nums[0]
        while low <= high:
            if nums[low] <= nums[high]:
                res = min(res, nums[low])
                break
            mid = (low + high) // 2
            res = min(nums[mid], res)
            if nums[low] <= nums[mid]: low = mid + 1
            else: high = mid - 1
        return res