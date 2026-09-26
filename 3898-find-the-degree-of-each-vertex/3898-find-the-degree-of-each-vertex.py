class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output=[]
        for row in matrix:
            output.append(sum(row))
        return output