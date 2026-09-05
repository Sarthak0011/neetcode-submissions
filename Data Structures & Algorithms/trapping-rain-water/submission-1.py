class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i-1])
            rightMax[n-i-1] = max(height[n-i-1], rightMax[n-i])

        totalWater = 0

        for i in range(n):
            h = min(leftMax[i], rightMax[i])
            currHeight = height[i]

            if currHeight < h:
                totalWater += (h - currHeight)

        return totalWater
