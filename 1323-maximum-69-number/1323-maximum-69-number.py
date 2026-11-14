class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for a in range(len(s)):
            if s[a] == '6':
                s = s[:a] + '9' + s[a+1:]
                break
        return int(s)