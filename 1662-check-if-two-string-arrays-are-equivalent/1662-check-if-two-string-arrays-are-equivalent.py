class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s=""
        ss=""
        for i in range(len(word1)):
            s+=word1[i]
        for j in range(len(word2)):
            ss+=word2[j]
        return s==ss