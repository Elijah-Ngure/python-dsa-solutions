# a.) PROBLEM
# LeetCode: #3: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Pattern: sliding window, hash Map
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# b.) PROBLEM STATEMENT
# Given as string s, find the length of longest substring without duplicate characters in that substring.

# c.) INTUITION
# We use a sliding window technique. we will use a pointer to store the start of a unique substring.
# Each time we will use a hash map to store the characters with their index value.
# Each iteration, we will check if the window representing the substring doesn't have any duplicate. (We check for duplicate by checking if the character is already defined in the dictionary)
# We slide the window if the current character is in the hash map, effectively removing its previous index from the window. (We get the index of the defined character and replace the start index of the window with its index + 1, we then replace the index of that character in the dictionary with the current index)
# In each iteration we also update the longest_length = max(longest_length, current_index - start_window + 1)

# d.) ALGORITHM
# 1. start_window = 0
# 2. char_dict = {}
# 3. longest_length = 0
# 4. for current_index, char in enumerate(s):
#       a.) if char in char_dict:
#               i.) start_window = char_dict[char] + 1
#
#       b.) char_dict[char] = current_index
# 
#       c.) longest_length = max(longest_length, (current_index - start_window + 1))
# 5. return longest_length

# e.) COMPLEXITY
# Time: O(n): we are looping through the string once.
# Space: O(n): storing the unique values in the string

# f.) EDGE CASES
# 1. empty string: we initialize the longest_length to zero and return it since the for loop won't be run
# 2. repeating character index (stored in the dictionary) is not in the sliding window (it is less than the start_window index): we use max(start_window, char_dict[char] + 1) to only use the next index if it is in the window index.

def lengthOfLongestSubstring(self, s: str) -> int:
    char_dict = {}
    start_window = 0
    longest_length = 0

    for current_index, char in enumerate(s):
        if char in char_dict:
            start_window = max(start_window, char_dict[char] + 1)

        longest_length = max(longest_length, (current_index - start_window + 1))
        
        char_dict[char] = current_index

    return longest_length
