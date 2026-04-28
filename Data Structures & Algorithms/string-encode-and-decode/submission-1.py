class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"{len(string)}#{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        n = len(s)

        decoded = []
        i = 0

        while i < n:
            length = 0

            while s[i] != '#':
                length = (length * 10) + (ord(s[i]) - ord('0'))
                i += 1
            
            # Skip #
            i += 1

            start = i
            end = i + length
            decoded.append(s[start:end])

            i = end
        
        return decoded