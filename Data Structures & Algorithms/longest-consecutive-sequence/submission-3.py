class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        st.update(nums)

        maxSequence = 0

        for num in st:
            if num-1 not in st:
                currMaxSequence = 1
                nextNumber = num + 1
                while nextNumber in st:
                    currMaxSequence += 1
                    nextNumber += 1
                maxSequence = max(maxSequence, currMaxSequence)
        
        return maxSequence

        