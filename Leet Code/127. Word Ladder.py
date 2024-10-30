class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        beginSet = {beginWord}
        endSet = {endWord}
        steps = 1
        while beginSet and endSet:
            wordSet -= beginSet
            steps += 1
            newSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    left = word[:i]
                    right = word[i+1:]
                    for c in string.ascii_lowercase:
                        newWord = left + c + right
                        if newWord in wordSet:
                            if newWord in endSet:
                                return steps
                            newSet.add(newWord)
            if len(beginSet) > len(endSet):
                beginSet = endSet
                endSet = newSet
            else:
                beginSet = newSet


        return 0