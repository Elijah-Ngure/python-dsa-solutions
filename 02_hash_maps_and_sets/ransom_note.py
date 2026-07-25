# a.) PROBLEM
# LeetCode: #383: Ransom Note
# Difficulty: Easy
# Pattern: string, hash table, counting
# Link: https://leetcode.com/problems/ransom-note/

# b.) PROBLEM STATEMENT
# Provided two strings: ransomNone and magazine, return True if ransomNote's characters are fully in magazine string, otherwise return False

# c.) INTUITION
# using Counter
# we convert the two strings into counters Counter(n), Counter(m)
# we check if Counter(m) <= Counter(n), return True if it is the case, else return False

# d.) ALGORITHM
# 1. check if Counter(m) <= Counter(n):
#   a.) return True
#   b.) Else: return False

# e.) COMPLEXITY
# Time: O(n + m): counting the frequency of ransomNote (m), and magazine (n) + check O(k1)
# Space: O(n + m): worst case where n and m have unique characters

# f.) EDGE CASES
# 1. no edge cases using Counter

from collections import Counter

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    return Counter(ransomNote) <= Counter(magazine)
