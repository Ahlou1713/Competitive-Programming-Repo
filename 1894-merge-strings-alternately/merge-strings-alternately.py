class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = []
        i = 0
        while(i < len(word1) and i < len(word2)):
            word3.append(word1[i])
            word3.append(word2[i])
            i += 1
        
        if(i < len(word1)):
            while(i < len(word1)):
                word3.append(word1[i])
                i += 1


        if(i < len(word2)):
            while(i < len(word2)):
                word3.append(word2[i])
                i += 1

        return ''.join([str(i) for i in word3])