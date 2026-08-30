class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n

        prefix[0] = nums[0]
        postfix[n-1] = nums[n-1]


        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i-1]
            postfix[n-i-1] = nums[n-i-1] * postfix[n-i]
        
        ans = []
        ans.append(postfix[1])

        for i in range(1, n-1):
            ans.append(prefix[i-1] * postfix[i+1])
        
        ans.append(prefix[n-2])

        return ans