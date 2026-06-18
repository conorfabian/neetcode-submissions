class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l, r = 0, 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if prices[r] < prices[l]:
                l = r
            else:
                r += 1

        return res