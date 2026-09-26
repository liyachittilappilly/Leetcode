class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        nn=""
        for i in range(len(str(n))-1,-1,-1):
            nn+=str(n)[i]
        return abs(n-(int(nn)))