class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def helper(index):
            if index >= len(nums):
                res.append(nums.copy())
                return

            for i in range(index, len(nums)):
                swap(nums, index, i)
                helper(index+1)
                swap(nums, index, i)

        helper(0)
        return res