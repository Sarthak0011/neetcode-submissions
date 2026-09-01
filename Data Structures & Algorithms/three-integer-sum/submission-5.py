class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        res = []

        for i in range(n-2):
            if(i > 0 and nums[i] == nums[i-1]): continue

            j = i + 1
            k = n - 1

            while j < k:
                n1 = nums[i]
                n2 = nums[j]
                n3 = nums[k]

                sum = n1 + n2 + n3

                if sum == 0:
                    res.append([n1, n2, n3])
                    j += 1
                    k -= 1

                    while(j < k and nums[j] == nums[j-1]): j += 1
                    while(j < k and nums[k] == nums[k+1]): k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return res



        