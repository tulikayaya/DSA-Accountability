class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            length = len(string)
            res += str(length) + '#' + string
        return res

    def decode(self, s: str) -> List[str]:
        i, res = 0, []

        while i < len(s):
            characters = ""

            while s[i] != '#':
                characters += s[i]
                i+=1
            
            i = i + 1
            length = int(characters)
            string = ""
            for j in range(length):
                string += s[i + j]
            
            res.append(string)
            i += length
        return res






