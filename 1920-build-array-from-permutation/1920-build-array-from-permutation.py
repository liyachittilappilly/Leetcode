class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        output=[]
        for i in range(len(nums)):
            output.append(nums[nums[i]])
        return output
