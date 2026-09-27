class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                output.append(0)
            else:
                output.append(1)
        output.sort()
        return output