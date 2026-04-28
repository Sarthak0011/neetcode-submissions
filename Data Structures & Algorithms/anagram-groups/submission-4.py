class Solution:
    def _generate_hash(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        hash_list = []
        for f in freq:
            hash_list.append(str(f))
            hash_list.append("#")
        return "".join(hash_list)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        groups = {}

        for word in strs:
            hash_key = self._generate_hash(word)
            if hash_key in groups:
                groups[hash_key].append(word)
            else:
                groups[hash_key] = []
                groups[hash_key].append(word)
        
        groups_list = []
        for group in groups.values():
            groups_list.append(group)
        return groups_list