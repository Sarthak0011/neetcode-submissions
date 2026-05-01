class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        output = [0] * n

        for i in range(n):
            curr_temperature = temperatures[i]
            while stack and curr_temperature > temperatures[stack[-1]]:
                output[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return output
