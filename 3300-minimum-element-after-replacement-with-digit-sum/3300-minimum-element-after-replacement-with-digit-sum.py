class Solution:
    def minElement(self, nums: List[int]) -> int:
        output=[]
        for i in range(len(nums)):
            s=[]
            o=0
            s=str(nums[i])
            for x in s:
                o+=int(x)
            output.append(o)
        
        return min(output)