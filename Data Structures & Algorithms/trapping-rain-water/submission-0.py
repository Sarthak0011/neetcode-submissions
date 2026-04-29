class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        # Initial Configuration
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        lm = 0
        rm = 0
        for i in range(n):
            leftMax[i] = lm
            rightMax[n-i-1] = rm

            lm = max(lm, height[i])
            rm = max(rm, height[n-i-1])
        
        maxWater = 0

        for i in range(n):
            currWater = min(leftMax[i], rightMax[i]) - height[i]
            if currWater > 0:
                maxWater += currWater
        
        return maxWater