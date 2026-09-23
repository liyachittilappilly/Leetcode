class Solution:
    def minimumSum(self, num: int) -> int:
        numm = []

        for i in str(num):
            numm.append(int(i))

        numm.sort()

        num1 = 0
        num1 += numm[0] * 10
        num1 += numm[2]

        num2 = 0
        num2 += numm[1] * 10
        num2 += numm[3]

        return num1 + num2