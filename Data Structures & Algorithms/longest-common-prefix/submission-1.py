class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""

        first_str = strs[0]

        for i in range(len(first_str)):
            for s in strs:
                if i == len(s) or s[i] != first_str[i]:
                    return longest_common_prefix
            longest_common_prefix += first_str[i]
        
        return longest_common_prefix