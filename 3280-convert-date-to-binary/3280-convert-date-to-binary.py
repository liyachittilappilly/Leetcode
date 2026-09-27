class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year=int(date[:4])
        month=int(date[5:7])
        datee=int(date[8:])
        year=bin(year)[2:]
        month=bin(month)[2:]
        datee=bin(datee)[2:]
        return year +"-"+month+"-"+datee