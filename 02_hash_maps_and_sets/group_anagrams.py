# a.) PROBLEM
# LeetCode: #49: Group Anagrams
# Difficulty: Medium
# Pattern: hash Map, sorting
# Link: https://leetcode.com/problems/group-anagrams/description/

# b.) PROBLEM STATEMENT
# Given an array of strings, group the anagrams in the array together and return the answer as a list of grouped anagrams in any order.

# c.) INTUITION
# Anagrams are words with same number of alphabets and similar sylables used. We use a hash map to store the representation of a particular hashmap (same sylables or number of symbols) then store every string in the array that has the same order as that particular hashmap, creating new entry when there is none with the similarity.

# OPTION 1: we sort the string before putting them in the hashmap, thus the sorted string becomes the representation pattern for its anagrams.
# With this, every other sorted string that is same as the sorted string becomes its anagram.
# Time complexity will be O(n*m log m) with m log m for sorting the string first and O(n) for traversing the string.

# OPTION 2: we use a tuple to represent the string's map in the 26 alphabets. We build the tuple then use the tuple as the key and store the strings as the values.
# Time complexity is O(n*m) where m will be traversing the string to create the tuple.

# d.) ALGORITHM
# 1. create an anagrams_dict = defaultdict(list)
# 2. a_index = ord("a")
# 2. for word in strs:
#   a.) frequency_tuple = [0] * 26
#   b.) for char in word:
#       i.) frequency_tuple[ord(char) - a_index] += 1
#   c.) anagrams_dict[frequency_tuple].append(word)
# 3. return list(anagrams_dict.values())

# e.) COMPLEXITY
# Time: O(n*m): O(m) for getting the words frequency tuple * O(n) for looping through the words in the list + O(k) for getting the lists of unique anagrams
# Space: O(n): Storing the anagrams in a hashmap + O(26) ~ O(1): storing the frequency tuple for the word.

# f.) EDGE CASES
# 1. storing a new unique string for the first time in the dictionary: the defaultdict(list) ensures it hanldes it internally without any errors.


from collections import defaultdict


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
    anagrams_dict = defaultdict(list)
    a_index = ord("a")

    for word in strs:
        frequency_tuple = [0] * 26
        # build the frequency tuple for the word
        for char in word:
            frequency_tuple[ord(char) - a_index] += 1
        
        anagrams_dict[tuple(frequency_tuple)].append(word)
    
    return list(anagrams_dict.values())

    
    # put the items from the dictionary into a final list
    return list(anagrams_dict.values())
