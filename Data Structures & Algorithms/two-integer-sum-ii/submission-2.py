class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        start = 0
        end = n-1

        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1, end+1]
            
            if sum > target:
                end -= 1
            else:
                start += 1

        return [-1, -1]