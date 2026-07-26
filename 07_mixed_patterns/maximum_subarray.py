# a.) PROBLEM
# LeetCode: #53: Maximum Subarray
# Difficulty: Easy
# Pattern: array, prefix sum
# Link: https://leetcode.com/problems/maximum-subarray/

# b.) PROBLEM STATEMENT
# Given an array of integers, find the largest sum you can get from a subbarray of the integers.

# c.) INTUITION
# the subarray may contain negative numbers, so that means that we need to keep two prefix sum (temp_sum and final_sum). temp_sum will keep the sum of the previous continous values so far (subarray).
# As we loop through the array, we update the temp_sum value with the current element to increase its value, but if the current value is larger than the current temp_sum, we replace the temp_sum with this value (effectively starting a new subarray)

# d.) ALGORITHM
# 1. initialize the temp_sum = final_sum = nums[0]
# 2. for index, value in enumerate(nums, start=1):
#   a.) temp_sum = max(value, temp_sum + value)
#   b.) final_sum = max(final_sum, temp_sum)
# 3. return final_sum

# e.) COMPLEXITY
# Time: O(n): looping through the values in the list
# Space: O(1): storing the prefix sum variables (temp_sum, final_sum)

# f.) EDGE CASES
# 1. list contains only one value: initialize the final_sum and temp_sum with the first element in the list

def maxSubArray(self, nums: List[int]) -> int:
    temp_sum = nums[0]
    final_sum = nums[0]

    # loop through the items in the list
    for index in range(1, len(nums)): 
        value = nums[index]
        # increase the subarray or start a new          
        temp_sum = max(value, temp_sum + value)
        # update global sum if it has been surpased
        final_sum = max(final_sum, temp_sum)
    
    return final_sum
