# a.) PROBLEM
# LeetCode: #1672: Richest Cutomer Wealth
# Difficulty: Easy
# Pattern: Array, prefix sum
# Link: https://leetcode.com/problems/richest-customer-wealth/

# b.) PROBLEM STATEMENT
# Given a grid list of customers and their accounts in different banks, find the customer with the most combined wealth among all the others.

# c.) INTUITION
# We store a max_wealth variable for holding the largest customer wealth value
# We check every customer's accounts, add all their total money in every account.
# we then update the max_wealth if this current customer's total money is greater than the current max_wealth value

# d.) ALGORITHEM
# 1. Initialize max_wealth variable
# 2. For each customer in the accounts list:
#   a.) compute the sum for all the user's accounts
#   b.) update max_wealth if the user's amount is greater than the max_wealth (max_wealth = max(max_wealth, user_amount))

# e.) COMPLEXITY
# Time: O(n x m) -> O(n) for looping through the customers X O(m) for summing up all accounts for each user
# Space: O(1) -> for storing the prefix sum (max_wealth)

# f.) EDGE CASES
# 1. Empty accounts: the loop is not run and the function return max_wealth of 0


def maximumWealth(self, accounts: List[List[int]]) -> int:
    max_wealth = 0
    for user_accounts in accounts:
        # add the money in all the user's accounts
        user_amount = sum(user_accounts)
        # update the max_wealth
        max_wealth = max(max_wealth, user_amount)
    
    return max_wealth
