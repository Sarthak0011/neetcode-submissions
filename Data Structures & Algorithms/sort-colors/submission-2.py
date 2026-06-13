class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0
        mid = 0
        high = n-1

        while mid <= high:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 0:
                self.swap(nums, low, mid)
                low += 1
                mid += 1
            else:
                self.swap(nums, mid, high)
                high -= 1
        