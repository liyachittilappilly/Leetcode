class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(len(pos)):
            output.append(pos[i])
            output.append(neg[i])

        return output