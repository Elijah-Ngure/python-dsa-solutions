# a.) PROBLEM
# LeetCode: #283: Move Zeroes
# Difficulty: Easy
# Pattern: array, two pointers
# Link: https://leetcode.com/problems/move-zeroes/

# b.) PROBLEM STATEMENT
# Given an array of integers, move all 0's to the end of the list while maintaining the sequential order of the non-zero elements.
# constraint: this must be done in-place without making a copy of the array

# c.) INTUITION
# We keep a pointer for tracking the last unassigned zero value (zero_index), we then loop through the list checking for non-zero values, when we find them, we put them at the last unassigned zero_index, then we increment the zero_index.

# d.) ALGORITHM
# 1. initialize zero_index = 0
# 2. for index, value in enumerate(nums):
#   a.) if value == 0: continue
#   b.) elif index > zero_index: 
#       i.) nums[zero_index] = value
# 3. zero_index += 1

# e.) COMPLEXITY
# Time: O(n): traversing through the list once
# Space: O(1): storing the zero_index

# f.) EDGE CASES
# 1. All values are zero. We just skip the values
# 2. No zero values in the list: We increment the zero_index as we loop through the list

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_index = 0

    for index, value in enumerate(nums):
        if value == 0:
            continue

        elif zero_index < index:
            # swap the values
            nums[zero_index], nums[index] = value, 0
            
        # increment the zero index
        zero_index += 1
                

        
