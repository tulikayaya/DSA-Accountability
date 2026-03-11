class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        lis = []

        for i in range(len(nums)):
            value = target - nums[i]
            for j in range(i+1, len(nums)):
                final_value = value - nums[j]
                ind = {}
                for k in range(j+1, len(nums)):
                    if final_value - nums[k] in ind:
                        fourplet = (nums[i], nums[j], final_value - nums[k], nums[k])
                        result.add(fourplet)
                    else:
                        ind[nums[k]] = k

        for fourplet in result:
            lis.append(list(fourplet))
        return lis

        