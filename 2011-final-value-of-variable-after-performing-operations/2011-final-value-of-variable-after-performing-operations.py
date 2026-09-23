class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        n=0
        for i in range(len(operations)):
            if operations[i]=="--X" or operations[i]=="X--":
                n-=1
            elif operations[i]=="X++" or operations[i]=="++X":
                n+=1
        return n