class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mpp = {}

        max_len = 0
        start = 0
        for i in range(n):
            if s[i] in mpp:
                new_start = mpp.get(s[i]) + 1
                if new_start > start:
                    start = new_start
            
            curr_len = i - start + 1
            max_len = max(max_len, curr_len)
            mpp[s[i]] = i
            
        return max_len