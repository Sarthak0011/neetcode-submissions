class Solution:
    def is_same(self, ch1: str, ch2: str) -> bool:
        return ch1.lower() == ch2.lower()

    def is_alpanumeric(self, ch: str) -> bool:
        return ((ch >= '0' and ch <= '9') or (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'))

    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while low < high:
            if not self.is_alpanumeric(s[low]):
                low += 1
                continue
            if not self.is_alpanumeric(s[high]):
                high -= 1
                continue
            
            if not self.is_same(s[low], s[high]):
                return False

            low += 1
            high -= 1
        
        return True


        