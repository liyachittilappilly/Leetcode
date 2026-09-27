class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            for a in words[i]:
                if a not in allowed:
                    break
            else:
                count+=1
        return count