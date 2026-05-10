class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        wordSet = set()
        for word in wordList: wordSet.add(word)
        # if beginWord not in wordSet: return 0

        q = deque()
        q.append([beginWord, 1])
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        ans = float("inf")
        while q:
            word, level = q.popleft()
            if word == endWord:
                ans = min(ans, level)
            
            for i in range(len(word)):
                for c in range(ord('a'), ord('z')+1):
                    ch = chr(c)
                    nextWord = word[:i] + ch + word[i+1:]
                    if nextWord in wordSet:
                        q.append([nextWord, level+1])
                        wordSet.remove(nextWord)
        if ans == float("inf"): return 0
        return ans