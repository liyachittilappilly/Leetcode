class Solution:
    def checkRecord(self, s: str) -> bool:
        countA=0
        countL=0
        for ss in s:
            if ss=="L":
                countL+=1
            else:
                countL=0
            if ss=="A":
                countA+=1
            if countA>=2 or countL>=3:
                return False
        
        return True