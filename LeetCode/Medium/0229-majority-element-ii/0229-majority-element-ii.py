class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2, ele1, ele2 = 0, 0, -inf, -inf
        lis = []

        for num in nums:
            if count1 == 0 and num != ele2:
                ele1 = num
                count1 += 1
            elif count2 == 0 and num != ele1:
                ele2 = num
                count2 += 1
            elif ele1 == num:
                count1+=1
            elif ele2 == num:
                count2+=1
            else:
                count1 -=1
                count2 -=1

        size = len(nums)    
        mini = size//3

        count1, count2 = 0, 0

        for num in nums:
            if num == ele1:
                count1 += 1
            if num == ele2:
                count2 += 1
        
        if count1 > mini:
            lis.append(ele1)
        if count2 > mini:
            lis.append(ele2)
            
        return lis
            

        