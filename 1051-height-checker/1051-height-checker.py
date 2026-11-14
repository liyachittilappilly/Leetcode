
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)

        for a in range(len(heights)):
            if heights[a] != expected[a]:
                count += 1

        return count
