class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit from a single buy and sell transaction.

        Strategy: Sliding Window
        - buy pointer tracks the cheapest price seen so far.
        - sell pointer scans forward looking for the best price to sell.
        - If we find a cheaper buy price, shift the buy pointer to it.
        """
        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):

            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)

            else:
                # Found a cheaper price to buy — shift buy pointer to it
                buy = sell

            sell += 1

        return max_profit