class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        output=[]
        maxx=max(nums)
        minn=min(nums)
        for i in range(minn,maxx):
            if i not in nums:
                output.append(i)
        return output