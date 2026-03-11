class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged = merged + word1[i]
            merged = merged + word2[j]
            i+=1
            j+=1

        if len(word1) > len(word2):
            while i < len(word1):
                merged = merged + word1[i]
                i+=1
        elif len(word2) > len(word1):
            while j < len(word2):
                merged = merged + word2[j]
                j+=1
        return merged

        