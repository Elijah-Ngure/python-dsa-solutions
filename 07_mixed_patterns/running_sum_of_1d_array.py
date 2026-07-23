# a.) PROBLEM
# LeetCode: #1480: Running Sum of 1d Array
# Difficulty: Easy
# Pattern: Array, prefix sum
# Link: https://leetcode.com/problems/running-sum-of-1d-array/

# b.) PROBLEM STATEMENT
# Given an array of number, replace the number in each index with the sum of all previous number including that particular number in that index

# c.) INTUITION
# We keep a prefix_sum variable that will store the sum of all previous values upto the current index
# For each index, we will add the number to the prefix_sum then replace that index with this prefix_sum

# d.) ALGORITHM
# 1. Initiate the prefix_sum to 1
# 2. For each index in the numbers list:
#      a.) Add the number in that particular index to the prefix_sum
#      b.) Replace the number in that particular index with the prefix_sum
# 3. return the numbers list

# e.) COMPLEXITY
# Time: O(n) -> we will traverse through the list adding the prefix sum onto the values
# Space: O(1) -> we store the prefix_sum and we reuse the same original numbers list for the updated values.

# f.) EDGE CASES
# 1. Negative numbers: included in the prefix_sum through addition (they decrement the prefix_sum value)
# 2. Empty list: we just return the original empty list
# 3. Only one number in the list: original value is added by 0 which doesn't change the value of the number in the list

def runningSum(self, nums: List[int]) -> List[int]:
    current_sum = 0
    for index in range(len(nums)):
        # update the current_sums
        current_sum = nums[index] + current_sum
        # combine the indexes with the total sum
        nums[index] = current_sum
    
    return nums
