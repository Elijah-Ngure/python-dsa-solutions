# a.) PROBLEM
# LeetCode: #125: Valid Palindrome
# Difficulty: Easy
# Pattern: array, two pointers
# Link: https://leetcode.com/problems/valid-palindrome/

# b.) PROBLEM STATEMENT
# Given a string, return True if is a valid palindrome, False otherwise.
# A palindrome is one where, the alphanumeric characters read the same forward and backwards regardless of their case. Meaning, the string could have non-alphanumeric characters but these are ignored.

# c.) INTUITION
# since a palindrome reads the same forward and backwards, the easiest way to check for a palindrome is to have two pointers.
# one from the begining (moving forward) of the string the other at the end (moving backwards) of the string.
# the alphanumeric characters should be the same when moving the pointers towards each other.

# d.) ALGORITHM
# 1. Initiate start pointer = 0
# 2. Initiate end pointer = len(string) - 1
# 3. while start < end:
#   a.) if string[start] and string[end] are both not alphanumeric:
#           i.) start += 1
#           ii.) end -= 1
#   b.) elif string[start] is not alphanumeric:
#           i.) skip the character: start+= 1
#   c.) elif string[end] is not alphanumeric:
#           i.) skip the character: end -= 1
#   d.) elif string[start].lower() != string[start].lower():
#           i.) return False
# 4. return True

# e.) COMPLEXITY
# Time: O(n): we traverse the list n/2 times by using the two pointers (start and end)
# Space: O(1): storing the two pointers: O(1) + O(1)

# f.) EDGE CASES
# 1. Empty string: we return True since it reads the same forwards and backwards.
# 2. String with pure alphanumerics: Since we ignore the alphanumerics, then by definition that string is empty hence we return True


def isPalindrome(self, s: str) -> bool:
    start = 0
    end = len(s) - 1

    while start < end:
        if not s[start].isalnum() and not s[end].isalnum():
            start += 1
            end -= 1
        elif not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
    
    return True
