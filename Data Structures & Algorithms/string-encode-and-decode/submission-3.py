class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded


    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        decoded = []

        while i < n:
            length = 0
            while s[i] != '#':
                length = (length * 10) + (ord(s[i]) - ord('0'))
                i += 1
            
            i += 1

            start = i
            end = i + length

            decoded.append(s[start:end])
            i = end
        return decoded