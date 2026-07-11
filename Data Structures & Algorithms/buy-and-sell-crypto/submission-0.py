class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price_so_far = prices[0]
        max_profit = 0

        for price in prices[1:]:
            lowest_price_so_far = min(lowest_price_so_far, price)
            max_profit = max(max_profit, price - lowest_price_so_far)

        return max_profit