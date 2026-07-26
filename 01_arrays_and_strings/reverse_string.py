# a.) PROBLEM
# LeetCode: #344: Reverse String
# Difficulty: Easy
# Pattern: array, two pointers
# Link: https://leetcode.com/problems/reverse-string/

# b.) PROBLEM STATEMENT
# Given an input of array characters, do an in-place reverse of the array with O(1) extra memory

# c.) INTUITION
# OPTION 1: use two pointers (forward, backwards), where we switch the elements in those pointer position with each other. After each operation, increment the forward pointer while decrementing the backwards pointer. Do this till the forward and backward pointers are equal.

# OPTION 2: use the in-build reverse() function, this uses under the hood C-level two pointers implementing OPTION 1 using a faster language (C)

# d.) ALGORITHM
# 1. string.reverse()

# e.) COMPLEXITY
# Time: O(n): the reverse() function loops through the list n/2 times swapping the elements in position.
# Space: O(1): uses two pointers (forward and backwards) and swaps the elements in-place

# f.) EDGE CASES
# 1. single item in the array: no need for swapping any elements

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()
        
