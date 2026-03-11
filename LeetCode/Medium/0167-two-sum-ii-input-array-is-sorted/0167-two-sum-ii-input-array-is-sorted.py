class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res, ind = [], {}
        for i in range(len(numbers)):
            if (target - numbers[i]) in ind:
                res.append(ind[target - numbers[i]])
                res.append(i+1)
                return res
            else:
                ind[numbers[i]] = i + 1
        return res
        