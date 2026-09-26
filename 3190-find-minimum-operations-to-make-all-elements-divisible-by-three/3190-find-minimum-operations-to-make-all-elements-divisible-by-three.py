class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        summ=sum(nums)
        kk=0
        for n in nums:
            if n%3!=0:
                kk+=1
        return kk