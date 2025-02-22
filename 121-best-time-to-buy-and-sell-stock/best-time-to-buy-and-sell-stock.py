class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        data = list()
        while i < len(prices) - 1:
            data.append(prices[i + 1] - prices[i])
            i += 1
        s = 0
        profit = 0
        for i in data:
            if i > 0:
                s = s + i
            else:
                profit = max(profit, s)
                s = 0 if s+i < 0 else s+i
        return max(profit, s)