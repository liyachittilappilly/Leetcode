class Solution:
    def maxDistinct(self, s: str) -> int:
        r=""
        for i in s:
            if i not in r:
                r+=i
        return len(r)
        