class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        element = nums[0]
        count = 1

        for i in range(1, n):
            if nums[i] != element and count == 0:
                element = nums[i]
                count = 1
            elif nums[i] == element:
                count += 1
            else:
                count -= 1
        return element