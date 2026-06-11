class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_arr = [0] * 26

        for i in range(len(s)):
            hash_arr[ord(s[i]) - ord('a')] += 1
            hash_arr[ord(t[i]) - ord('a')] -= 1
        
        for freq in hash_arr:
            if freq != 0: return False
        
        return True