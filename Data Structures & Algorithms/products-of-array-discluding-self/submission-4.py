class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i-1]
            suffix[n-i-1] = nums[n-i-1] * suffix[n-i]
        
        output = []
        for i in range(n):
            pre = 1 if i == 0 else prefix[i-1]
            suf = 1 if i == n-1 else suffix[i+1]

            output.append(pre * suf)
        
        return output

