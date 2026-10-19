class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        if coordinate1[0] in 'aceg':
            if int(coordinate1[1]) % 2 == 0:
                result = True
            else:
                result = False
        else:
            if int(coordinate1[1]) % 2 == 0:
                result = False
            else:
                result = True

        if coordinate2[0] in 'aceg':
            if int(coordinate2[1]) % 2 == 0:
                resultt = True
            else:
                resultt = False
        else:
            if int(coordinate2[1]) % 2 == 0:
                resultt = False
            else:
                resultt = True

        if result == resultt:
            return True
        else:
            return False