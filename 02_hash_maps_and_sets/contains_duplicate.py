# a.) PROBLEM
# LeetCode: #217: Contains Duplicate
# Difficulty: Easy
# Pattern: hash table
# Link: https://leetcode.com/problems/contains-duplicate/

# b.) PROBLEM STATEMENT
# Given an array of integers, return True if any integer value appears twice in the array list

# c.) INTUITION
# We can loop through the list, appending the numbers into a set.
# On each list iteration, we check if the number is in the set, if so, then a duplicate has occurred, else we just add the new number in the set.
# If we have reached the end of the list without a duplicate, we return False

# d.) ALGORITHM
# 1. Initialize a new nums_set = set()
# 2. for number in nums:
#   a.) if number in nums_set:
#       return False
#   b.) Else: nums_set.append(number)
# 3. return False

# e.) COMPLEXITY
# Time: O(n): traversing through the list once
# Space: O(n): storing the list items in the set

# f.) EDGE CASES
# 1. no edge cases

def containsDuplicate(self, nums: List[int]) -> bool:
    nums_set = set()
    # loop through the nums of list adding to the set
    # if the digit has been added already -- it is a duplicate (return False)
    # If we add all values in the set -- no duplicates (return True)
    for number in nums:
        if number in nums_set:
            return True
        else:
            # add the number in the set
            nums_set.add(number)
    
    return False
