# a.) PROBLEM
# LeetCode: #121: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Pattern: array, prefix sum
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# b.) PROBLEM STATEMENT
# Given an array of stock prices, calculate the maximum profit you can get when you choose a specific day to buy a stock and another day in the future to sell that stock.
# Keeping in mind that you cannot sell that stock a day prior to the day you bought that stock. And if there is no day to make any profit, just return 0

# c.) INTUITION
# have a variable (min_buy_price), we can sequentially minus the min_buy_price from the array values, storing the difference using a prefix sum if it exceeds it (max_profit). With each iteration, we update the min_buy_price if the current price is lower than the previous min_buy_price.
# With that we will get the most minimum and maximum price different across continuous sequential days.

# d.) ALGORITHM
# 1. Initialize the min_buy_price = prices[0]
# 2. Initialize max_profit = 0
# 3. for stock_price in prices:
#   a.) max_profit = max(stock_price - min_buy_price)
#   b.) min_buy_price = min(min_buy_price, stock_price)
# 4. return max_profit

# e.) COMPLEXITY
# Time: O(n): we traverse the list once
# Space: O(1): storing prefix sum (max_profit) and min_buy_price

# f.) EDGE CASES
# 1. single stock price in the prices: The loop runs once, hence subtracting the same min_buy_price and stock_price getting 0, no profit.


def maxProfit(self, prices: List[int]) -> int:
    # hold values for the profit, buying
    # The biggest difference between buying and selling will be the most profit        
    max_profit = 0
    min_buy_price = prices[0]

    for stock_price in prices:
        # calculate the profit and save the bigger one
        max_profit = max((stock_price - min_buy_price), max_profit)
        # update the min buy price if the stock price is less than it
        min_buy_price = min(stock_price, min_buy_price)
    
    return max_profit
