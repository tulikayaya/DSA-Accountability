class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        res = []

        for string in strs:
            p = tuple(sorted(string))
            dic[p].append(string)

        for key, value_list in dic.items():
            res.append(value_list)
        return res

        

