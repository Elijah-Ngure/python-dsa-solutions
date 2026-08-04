# a.) PROBLEM
# LeetCode: #2363: Merge Similar Items
# Difficulty: Easy
# Pattern: hash map, array
# Link: https://leetcode.com/problems/merge-similar-items/

# b.) PROBLEM STATEMENT
# Given two 2D integer arrays, where each contains and item [value, weight], merge the two list together by their value where items with similar value have weight combined into one. Return the final list sorted in ascending order by value

# c.) INTUITION
# Since the two lists could contain duplicate items values, we use a hash map to store the unique values.
# Instead of looping over the lists one by one, we could get the largest length of the two lists.
# We then loop over the two lists simultaneously.
# We add the values to the hash Map, each time incrementing the weights with the one already in the hash Map.
# After iterating the two lists, we then sort the items in the hash Map and return them.

# d.) ALGORITHM
# 1. consolidated_map = defaultdict(int)
# 2. items1_length = len(items1)
# 3. items2_length = len(items2)
# 4. max_length = max(items1_length, items2_length)
# 5. for index in range(max_length):
#       a.) if index < items1_length:
#           i.) item = items1[index]
#           ii.) consolidated_map[item[0]] += item[1]
#
#       b.) if index < items2_length:
#           i.) item = items2[index]
#           ii.) consolidated_map[item[0]] += item[1]
#
# 6. return list(sorted(consolidated_map))

# e.) COMPLEXITY
# Time: O(n log n): sorting the final list O(n log n) + iterating through the items to consolidate them into the hashMap: O(n)
# Space: O(n): storing the consolidated items in the hash Map


from collections import defaultdict

def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    consolidated_map = defaultdict(int)

    items1_length = len(items1)
    items2_length = len(items2)
    max_length = max(items1_length, items2_length)

    for index in range(max_length):
        # get the value of the first list
        if index < items1_length:
            item = items1[index]
            consolidated_map[item[0]] += item[1]

        # get the value of the second list
        if index < items2_length:
            item = items2[index]
            consolidated_map[item[0]] += item[1]
    
    return [[k, consolidated_map[k]] for k in sorted(consolidated_map)]
        
