
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num = []
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                num.append(nums[i])
        return sum(num)
