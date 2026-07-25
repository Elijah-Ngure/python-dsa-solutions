# a.) PROBLEM
# LeetCode: #242: Valid Anagram
# Difficulty: Easy
# Pattern: string, hash table, counting, Counter
# Link: https://leetcode.com/problems/valid-anagram/

# b.) PROBLEM STATEMENT
# Given two string, return True if they are anagrams of each other

# c.) INTUITION
# An anagram means that two strings have equal number of characters and same characters which may be arranged in different way.
# OPTION 1: after checking that they are the same length, we proceed to sort the strings, then check if one is in the other, if so return True, otherwise return False

# OPTION 2: Use Counter
# convert the two string to frequency dictionary using Counter,
# then check if they are equal

# d.) ALGORITHM
# 1. if len(s) != len(t):
#   a.) return False
# 2. return Counter(s) == Counter(t)

# e.) COMPLEXITY
# Time: O(n): getting the count of the strings O(n) + O(n), since they are equal in length
# Space: O(n): worst case when all alphabets in the string are unique

# f.) EDGE CASES
# 1. Unequal length of strings: we check if the two strings are equal and return False if they are not.

from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return Counter(s) == Counter(t)
