class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxi = 0
        for i in range(n):
            area = heights[i]

            for j in range(i-1, -1, -1):
                if heights[j] < heights[i]:
                    break
                area += heights[i]

            for j in range(i+1, n):
                if heights[j] < heights[i]:
                    break
                area += heights[i]

            maxi = max(maxi, area)
        
        return maxi