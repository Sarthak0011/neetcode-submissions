class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        low = 0
        high = len(heights) - 1

        while low < high:
            height = min(heights[low], heights[high])
            width = high - low

            water = height * width
            maxWater = max(maxWater, water)

            if heights[low] <= heights[high]:
                low += 1
            else:
                high -= 1

        return maxWater