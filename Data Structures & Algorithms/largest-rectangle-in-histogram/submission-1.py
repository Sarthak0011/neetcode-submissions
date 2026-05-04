class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # will contain [height, index]
        max_area = 0

        for i, h in enumerate(heights):
            start_index = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                start_index = index     # because we can push the index backwards
            stack.append([h, start_index])
        
        while stack:
            height, index = stack.pop()
            area = height * (n - index)
            max_area = max(max_area, area)
        
        return max_area
        
