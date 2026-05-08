class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ds = []

        def helper(index, target):
            if index >= len(nums):
                if target == 0:
                    res.append(ds.copy())
                return
            
            # not-pick
            helper(index+1, target)

            # pick
            if (target - nums[index]) >= 0:
                ds.append(nums[index])
                helper(index, target - nums[index])
                ds.pop()
        
        helper(0, target)
        return res
