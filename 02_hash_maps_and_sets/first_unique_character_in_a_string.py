# a.) PROBLEM
# LeetCode: #387: First Unique Character in a String
# Difficulty: Easy
# Pattern: Hash Map
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/

# b.) PROBLEM STATEMENT
# Given a string s, return the index of the first non-repeating character if it exists, else return -1

# c.) INTUITION
# Since we want the index of the value, we can use a dictionary map to store the characters and their index, where when we encounter a repeating character, we simply update its index in the dictionary with -1 because that character is invalid.
# Then we loop over the items in the dictionary (since it arranges the characters by order of insertion) returning the first item without -1

# d.) ALGORITHM
# 1. Initailize the hash map: chars_dict = {}
# 2. for index in range(len(s)):
#   a.) if s[index] in chars_dict:
#       i.) chars_dict[s[index]] = -1
#   b.) Else: 
#       ii.) chars_dict[s[index]] = index
# 
# 3. for key, value in chars_dict.items():
#   a.) if value != -1: return value
# 4. return -1

# e.) COMPLEXITY
# Time: O(n): putting the characters into the hash map O(n) + checking for the first unique character index: O(n) (worst case when the unique character is at the end of the string)
# Space: O(1): since there are only 26 unique characters of lowercase letter thus O(26) which is just O(1)

# f.) EDGE CASES
# 1. Empty string: it return -1

def firstUniqChar(self, s: str) -> int:
    chars_dict = {}

    for index in range(len(s)):
        # add the first index in the dictionary
        if s[index] in chars_dict:
            chars_dict[s[index]] = -1
        else:
            chars_dict[s[index]] = index

    
    # loop through the dictionary items for the first unique item
    for key, value in chars_dict.items():
        if value != -1:
            return value
    
    return -1
            
