from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = float("-inf")
        lower= float("inf")
        prices.pop(0)
        for price in prices:
            if price < low and price < lower:
                lower = price
            if price > high:
                high = price
                if lower < low:
                    low = lower
            elif (price - lower) > (high - low):
                high = price
                low = lower
                
        if high > low:
            print("high: ", high)
            print("low: ", low)
            return(high-low)
        else:
            return 0

# Test the code
sol = Solution()
prices = [7,4,1,2]
print("Max Profit:", sol.maxProfit(prices))

# Better solution
# class Solution:
    # def maxProfit(prices):
    #     min_price, max_profit = float('inf'), 0
    #     for p in prices:
    #         if p < min_price:
    #             min_price = p
    #         elif p - min_price > max_profit:
    #             max_profit = p - min_price
    #     return max_profit

# improvements: always lowers price but only updates profit when profit can be increased...
# works bc we only need to return profit, not high and low