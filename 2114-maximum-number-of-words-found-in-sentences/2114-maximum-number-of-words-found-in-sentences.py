class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maximum=0
        
        for i in range(len(sentences)):
            count=0
            for i in sentences[i]:

                if i ==" ":
                    count+=1
            maximum=max(maximum,count)
        return maximum+1