class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        s = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                s += prices[i+1] - prices[i]
            i += 1
        return s    