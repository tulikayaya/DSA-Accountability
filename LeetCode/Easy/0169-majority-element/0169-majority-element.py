class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, ele = 0, -inf

        for num in nums:
            if ele == num:
                count += 1
            elif count == 0:
                ele = num
                count = 1
            else:
                count -= 1

        return ele
        