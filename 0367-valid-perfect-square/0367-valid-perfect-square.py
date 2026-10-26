class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(100000):
            if num == i*i:
                return True
        return False