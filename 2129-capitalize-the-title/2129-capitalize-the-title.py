class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        output = title.split(" ")

        for i in range(len(output)):
            if len(output[i]) <= 2:
                result.append(output[i].lower())
            else:
                result.append(output[i].capitalize())

        return " ".join(result)