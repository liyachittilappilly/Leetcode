class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        summ=sum(nums)
        kk=0
        while summ%k!=0:
            summ-=1
            kk+=1
        return kk