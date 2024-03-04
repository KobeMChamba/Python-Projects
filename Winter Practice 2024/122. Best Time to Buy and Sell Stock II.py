class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float("inf")
        for price in prices:
            if price < low:
                low = price
            if price > low:
                profit += price - low
                low = price
        return profit
