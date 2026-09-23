class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        a=""
        for i in range(len(s)):
            a+=s[indices.index(i)]
        return a