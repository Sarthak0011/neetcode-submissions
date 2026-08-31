class Solution:
    def __isAlphaNumeric(self, c: str) -> bool:
        return (
            (c >= 'A' and c <= 'Z') or 
            (c >= 'a' and c <= 'z') or 
            (c >= '0' and c <= '9')
            )

    def __isSame(self, c1: str, c2: str) -> bool:
        return (c1.lower() == c2.lower())
    
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        start = 0
        end = n-1

        while start < end:
            if not self.__isAlphaNumeric(s[start]):
                start += 1
                continue
            if not self.__isAlphaNumeric(s[end]):
                end -= 1
                continue

            if not self.__isSame(s[start], s[end]):
                return False

            start += 1
            end -= 1
        
        return True
