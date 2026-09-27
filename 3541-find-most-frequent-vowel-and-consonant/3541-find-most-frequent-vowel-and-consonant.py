class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = "aeiou"
        consonant = ""
        
        for i in s:
            if i not in vowel:
                consonant += i
        
        uniqueV = ""
        uniqueC = ""

        for i in s:
            if i in vowel and i not in uniqueV:
                uniqueV += i
            elif i in consonant and i not in uniqueC:
                uniqueC += i

        frequencyV = []
        for i in uniqueV:
            count = 0
            for j in s:
                if i == j:
                    count += 1
            frequencyV.append(count)

        frequencyC = []
        for i in uniqueC:
            count = 0
            for j in s:
                if i == j:
                    count += 1
            frequencyC.append(count)

        maxV = max(frequencyV, default=0)
        maxC = max(frequencyC, default=0)

        return maxV + maxC