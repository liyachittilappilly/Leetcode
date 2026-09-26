class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        output=[]
        for i in range(len(order)):
            for j in range(len(friends)):
                if order[i]==friends[j]:
                    output.append(order[i])
        return output