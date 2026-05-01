class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def solve(self, index, nums, ans):
        if index >= len(nums):
            ans.append(nums.copy())
            return

        for i in range(index, len(nums)):
            self.swap(nums, index, i)
            self.solve(index+1, nums, ans)
            self.swap(nums, index, i)
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve(0, nums, ans)
        return ans