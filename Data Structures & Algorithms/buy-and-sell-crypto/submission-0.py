class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        res = []
        buy = 0
        sell = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            res.append(prices[sell]- prices[buy])
            sell += 1
        return max(res)
