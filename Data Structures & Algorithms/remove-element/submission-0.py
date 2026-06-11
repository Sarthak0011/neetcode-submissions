class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0   # i will be on the first occ of 'val'
        while i < n:
            if nums[i] == val:
                break
            i += 1
        
        j = i+1
        while j < n:
            if nums[j] == val:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                while i < n and nums[i] != val:
                    i += 1
                j = i+1
        return i