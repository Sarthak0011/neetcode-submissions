class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mpp = {}
        startIndex = 0

        maxLen = 0

        for i in range(n):
            if s[i] in mpp:
                newStartIndex = mpp[s[i]] + 1
                if newStartIndex > startIndex:
                    startIndex = newStartIndex
            
            currLen = i - startIndex + 1
            maxLen = max(maxLen, currLen)
            mpp[s[i]] = i
        return maxLen
