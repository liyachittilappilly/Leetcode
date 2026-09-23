class Solution(object):
    def numberOfMatches(self, n):
        nn = 0

        while n != 1:
            nn += n // 2
            n = (n + 1) // 2

        return nn