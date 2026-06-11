class Solution:
    def __generate_hash(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        hash_list = []
        for f in freq:
            hash_list.append(str(f))
            hash_list.append("#")
        return "".join(hash_list)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            curr_hash = self.__generate_hash(s)
            groups.setdefault(curr_hash, []).append(s)
        
        grouped_anagrams = []

        for words in groups.values():
            grouped_anagrams.append(words)
        return grouped_anagrams
            