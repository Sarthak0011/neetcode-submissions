class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            if key in mpp:
                mpp[key].append(s)
            else:
                mpp[key] = [s]
        ans = []
        for anagrams in mpp.values():
            ans.append(anagrams)
        return ans