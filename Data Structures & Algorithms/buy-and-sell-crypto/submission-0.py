class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_date = 0
        profit = 0 

        for d in range(len(prices)):
            # buy low 
            if prices[d] < prices[buy_date]:
                buy_date = d

            curr_profit = prices[d] - prices[buy_date]
            profit = max(profit, curr_profit)



        return profit