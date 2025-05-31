class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] is the price on the ith day.
        # want to maximize profit by choosing a single day to buy 1 stock and a different day in the future to sell it
        # return max profit or 0
        # => for each r, find a min l, then compare this with max_profit

        max_profit = 0
        min_l = prices[0]
        for curr_price in prices:
            if curr_price > min_l:
                max_profit = max(max_profit, curr_price - min_l)
            min_l = min(min_l, curr_price)
        return max_profit 