class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                max_profit = max(max_profit, price - buy)
        
        return max_profit
