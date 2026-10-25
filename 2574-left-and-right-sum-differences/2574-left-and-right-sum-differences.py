class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            leftsum=sum(nums[:i])
            rightsum=sum(nums[i+1:])
            answer.append(abs(leftsum-rightsum))
        return answer