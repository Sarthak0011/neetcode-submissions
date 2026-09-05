class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        ans = 0

        while start < end:
            curr_ans = min(heights[start], heights[end]) * (end - start)
            ans = max(ans, curr_ans)
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return ans