class Solution:
    def findMin(self, nums: list[int]) -> int:
        minimum=1000
        for i in range(len(nums)):
            minimum=min(minimum,nums[i])
        return minimum