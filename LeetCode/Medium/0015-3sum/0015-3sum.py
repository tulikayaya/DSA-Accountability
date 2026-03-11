class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lis = []
        ind = {}
        result = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            target = 0 - nums[i]
            ind = {}
            for j in range(i+1, len(nums)):
                if target - nums[j] in ind:
                    triplet = (nums[i], target - nums[j], nums[j])
                    result.add(triplet)
                else:
                    ind[nums[j]] = j

        for triplet in result:
            lis.append(list(triplet))
        return lis
        