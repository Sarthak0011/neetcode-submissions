class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""

        min_len = float("inf")
        for s in strs:
            min_len = min(min_len, len(s))

        for i in range(min_len):
            first_str = strs[0]
            flag = True
            for idx in range(1, len(strs)):
                curr_str = strs[idx]
                if first_str[i] != curr_str[i]:
                    flag = False
                    break
            if not flag:
                return longest_common_prefix
            longest_common_prefix += first_str[i]
        return longest_common_prefix