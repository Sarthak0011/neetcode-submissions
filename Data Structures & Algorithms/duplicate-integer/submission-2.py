class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        st = set()

        for num in nums:
            if num in st:
                return True
            else:
                st.add(num)
        return False
        