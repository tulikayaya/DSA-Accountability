class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        length = len(nums)
        res = [0] * length

        for i in range(len(nums)):
            index = (i+k)%length
            res[index] = nums[i]

        for j in range(len(res)):
            nums[j] = res[j]


            

        
        