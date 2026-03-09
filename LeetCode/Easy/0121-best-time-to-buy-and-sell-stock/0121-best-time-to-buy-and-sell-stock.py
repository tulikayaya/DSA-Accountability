class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, maxP = 0, 1, 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right #shifting to the NEXT minimum
            elif prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            right += 1
        return maxP

        