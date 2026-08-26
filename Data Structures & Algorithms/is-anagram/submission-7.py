class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] += 1
            hash[ord(t[i]) - ord('a')] -= 1
        
        for freq in hash:
            if freq != 0:
                return False
        return True