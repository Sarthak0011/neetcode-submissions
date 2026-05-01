class Solution:
    def solve(self, nums: List[int], index: int, curr_sum: int, target: int, combination: List[int], combinations: List[List[int]]):
        if index == len(nums):
            if curr_sum == target:
                combinations.append(combination.copy())
            return

        # not take
        self.solve(nums, index+1, curr_sum, target, combination, combinations)

        # take
        if curr_sum + nums[index] <= target:
            curr_sum += nums[index]
            combination.append(nums[index])
            self.solve(nums, index, curr_sum, target, combination, combinations)
            combination.pop()
            curr_sum -= nums[index]

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []

        self.solve(nums, 0, 0, target, combination, combinations)
        return combinations