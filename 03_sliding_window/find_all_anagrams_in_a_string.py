# a.) PROBLEM
# LeetCode: #438: Find All Anagrams in a String
# Difficulty: Medium
# Pattern: sliding window, string, hash Map
# Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

# b.) PROBLEM STATEMENT
# Given two strings: main string (s) and anagram string (p), find all the starting indices of p's anagram in main string (s). Return the list of indices found in any order.

# c.) INTUITION
# We use a sliding window technique. we'll keep track of window_start, Counter for the anagram and another counter for the window.
# we will traverse the list equating the frequency count of anagram (p) to frequency count of the window substring of equal length. (This will check if they are anagrams)
# Each iteration adds the character of the main string into the window (update the window Counter with the character)
# when the window becomes equal to the length of the anagram (p):
# i.) we check if the anagram Counter == window Counter (if so, we add the window_start index to the final indices)
# ii.) we subtract the main string (s[window_index]) from the window Counter
# iii.) we increment the window_start (shrinking the window
# this algorithm will have a time conmplexity of about O(n*m)

# We could further improve the algorithm to O(n + m) by keeping track of the number of matched characters of the current window substring against the anagram.
# we first store the anagram string (p) in a frequency dictionary with: key = character and value = tuple storing match frequency and anagram frequency i.e (match_frequency, anagram_frequency)
# we then keep a match variable (for storing the window substring's match against the anagram)
# we then iterate the main string, each time checking against the anagram's frequency dict for that particular character.
# i.) if the character exists in the anagram's dict, we'll get its tuple (match_frequency, anagram_frequency) and if match_frequency < anagram_frequency we increment the match frequency, together with the match_frequency in the tuple
# ii.) when shrinking the window, we check for match of that character in the frequency dict, and decrement match and match_frequency if it exists.

# d.) ALGORITHM
# 1. window_start = 0
# 2. final_indices = []
# 3. anagram_len = len(p)

# 4. if s < anagram_len: return final_indices

# 5. anagram_dict = {}
# 6. for index, value in enumerate(p):
# 7.    a.) if value in anagram_dict:
#           i.)anagram_dict[value] = (0, anagram_dict[value][1] + 1)
#       b.) Else: 
#            i.) anagram_dict[value] = (0, 1)
# 
# 8. anagram_match = 0

# 9. for index, value in enumerate(s):
#       a.) if value in anagram_dict:
#               i.) a_tuple = anagram_dict[value]
#               ii.) if a_tuple[0] < a_tuple[1]:
#                   1.) anagram_match += 1
#               iii.) anagram_dict[value] = (a_tuple[0] + 1, a_tuple[1])

#       b.) if (index - window_start + 1) >= anagram_len:
#               i.) if anagram_match == anagram_len:  final_indices.append(window_counter)
#               ii.) if s[window_start] in anagram_dict:
#                       1.) a_tuple = anagram_dict[s[window_start]]
#                       2.) if a_tuple[0] <= a_tuple[1]:
#                               i.) anagram_match -= 1
#                       3.) anagram_dict[s[window_start]] = (a_tuple[0] -1, a_tuple[1])
#                       
#               iii.) window_start += 1
#
# 10. return final_indices


# e.) COMPLEXITY
# Time: O(n): traversing the anagram string to create the frequency dict: O(m) + traversing through the main string (s) once O(n)
# Space: O(k): storing the frequency values for m


# f.) EDGE CASES
# 1. the main string (s) is less than the anagram string (p): we return an empty list
# 2. The match_frequency is greater than anagram_frequency in the anagram_dict for a particular character value: we don't update the match_frequency (either incrementing it or decrementing it)

def findAnagrams(self, s: str, p: str) -> List[int]:
    window_start = 0
    anagram_match = 0
    final_indices = []
    anagram_len = len(p)

    if len(s) < anagram_len: return final_indices

    anagram_dict = {}

    # create the anagram frequency tuple: (frequency_match, anagram_frequency)
    for index, value in enumerate(p):
        if value in anagram_dict:
            a_tuple = anagram_dict[value]
            anagram_dict[value] = (a_tuple[0], a_tuple[1] + 1)
        else:
            anagram_dict[value] = (0, 1)

    # check for matches of main string(s) in anagram_dict
    for index, value in enumerate(s):
        # slide the window
        if value in anagram_dict:
            a_tuple = anagram_dict[value]
            if a_tuple[0] < a_tuple[1]:
                anagram_match += 1

            anagram_dict[value] = (a_tuple[0] + 1, a_tuple[1])


        if (index - window_start + 1) >= anagram_len:
            if anagram_match == anagram_len: final_indices.append(window_start)

            # shrink the window
            start_char = s[window_start]
            if start_char in anagram_dict:
                a_tuple = anagram_dict[start_char]
                if a_tuple[0] <= a_tuple[1]:
                    anagram_match -= 1  
                anagram_dict[start_char] = (a_tuple[0] -1, a_tuple[1])

            window_start += 1
    
    return final_indices
            

