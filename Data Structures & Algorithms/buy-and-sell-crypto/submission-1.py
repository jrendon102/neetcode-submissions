class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        max_profit = 0

        while ptr1 < len(prices) and ptr2 < len(prices):
            profit = prices[ptr2] - prices[ptr1]
            if profit < 0:
                ptr1 += 1
            else:
                ptr2 += 1
            max_profit = max(profit, max_profit)
        return max_profit



            