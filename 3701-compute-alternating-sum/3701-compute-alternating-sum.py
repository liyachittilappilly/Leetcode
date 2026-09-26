class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n=[]
        for i in range(len(nums)):
            if i%2==0:
                n.append(nums[i]*-1)
            else:
                n.append(nums[i])
        return -sum(n)