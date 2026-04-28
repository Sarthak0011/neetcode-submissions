class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        n = len(s)
        hash = [0] * 26

        for i in range(n):
            hash[ord(s[i]) - ord('a')] += 1
            hash[ord(t[i]) - ord('a')] -= 1
        
        for freq in hash:
            if freq != 0:
                return False
        
        return True
        