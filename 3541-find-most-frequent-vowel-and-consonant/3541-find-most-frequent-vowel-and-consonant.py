class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowel = "aeiou"
        consonant = ""

        # Step 1: Store all consonants
        for i in s:
            if i not in vowel:
                consonant += i

        # Step 2: Find unique vowels and consonants
        uniqueV = ""
        uniqueC = ""

        for i in s:

            if i in vowel:

                if i not in uniqueV:
                    uniqueV += i

            else:

                if i in consonant:

                    if i not in uniqueC:
                        uniqueC += i

        # Step 3: Find frequency of each unique vowel
        frequencyV = []

        for i in uniqueV:

            count = 0

            for j in s:

                if i == j:
                    count += 1

            frequencyV.append(count)

        # Step 4: Find frequency of each unique consonant
        frequencyC = []

        for i in uniqueC:

            count = 0

            for j in s:

                if i == j:
                    count += 1

            frequencyC.append(count)

        # Step 5: Find maximum frequency
        maxV = max(frequencyV, default=0)
        maxC = max(frequencyC, default=0)

        # Step 6: Return answer
        return maxV + maxC