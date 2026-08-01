# a.) PROBLEM
# LeetCode: #209: Minimum Size Subarray Sum
# Difficulty: Medium
# Pattern: sliding window, prefix sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/

# b.) PROBLEM STATEMENT
# Given an array of positive integer values and a target sum, return the minimal length of a subarray that is greater than or equal to the target sum. If there is no such subarray, return 0 instead.

# c.) INTUITION
# We use a sliding window technique, where we keep track of the start_window index, minimum_size, prefix sum.
# We iterate through the array, sliding the window over it, (summing the values to the prefix sum) when the target hasn't been reached.
# When the target is reached:
# i.) we get the length of subbaray of the window (current_index - start_window + 1)
# ii.) update the minimum_size if current window size is less than the minimum_size
# iii.) Shrink the window until it doesn't violate the condition (< target sum), each time updating the start_window (+1),  minimum_size (min(minimum_size, current window size))

# d.) ALGORITHM
# 1. start_window = 0
# 2. prefix_sum = 0
# 3. minimum_size = 0
# 4. for current_index, value in enumerate(nums):
#       a.) if value == target: return 1
#       b.) prefix_sum += value
#       c.) while prefix_sum >= target:
#               i.) subarray_size = current_index - start_window +1
#               ii.) minimum_size = min(minimum_size, subarray_size) if minimum_size > 0 else subarray_size
#               iii.) prefix_sum -= nums[start_window]
#               iv.) start_window += 1
# 
# 5. return minimum_size

# e.) COMPLEXITY
# Time: O(n): Looping through the main list once O(n) + O(m): when shrinking the window
# Space: O(1): storing the prefix_sum, minimum_size and start_window variables

# f.) EDGE CASES:
# 1. Empty list: we return the minimum_size without iterating the list, which is already initialized to )
# 2. 

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    start_window = 0
    minimum_size = 0
    prefix_sum = 0

    for current_index, value in enumerate(nums):
        if value == target: return 1
        # expand the window
        prefix_sum += value

        # shrink the window
        while prefix_sum >= target:
            subarray_size = current_index - start_window + 1

            minimum_size = min(minimum_size, subarray_size) if minimum_size > 0 else subarray_size

            prefix_sum -= nums[start_window]

            start_window += 1
    
    return minimum_size
