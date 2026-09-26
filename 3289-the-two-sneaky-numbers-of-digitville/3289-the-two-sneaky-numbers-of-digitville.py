class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and nums[i] not in a:
                    a.append(nums[i])
        return a