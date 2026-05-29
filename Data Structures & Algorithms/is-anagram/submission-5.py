class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashArr = [0] * 26
        n = len(s)

        for i in range(n):
            ch1 = ord(s[i]) - ord('a')
            ch2 = ord(t[i]) - ord('a')

            hashArr[ch1] += 1
            hashArr[ch2] -= 1
        
        for i in range(26):
            if hashArr[i] != 0:
                return False
        return True