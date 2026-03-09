class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        res = []
        
        for i in range(len(nums)):
            if (target - nums[i]) in ind:
                res.append(ind[target - nums[i]])
                res.append(i)
                break
            else:
                ind[nums[i]] = i
        
        return res

        
        