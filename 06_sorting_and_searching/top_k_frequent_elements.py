# a.) PROBLEM
# LeetCode: #347: Top K Frequent Elements
# Difficulty: Medium
# Pattern: counter, hash Map
# Link: https://leetcode.com/problems/top-k-frequent-elements/

# b.) PROBLEM STATEMENT
# Given an integer of nums, return the k most frequent elements in the list in any order when given an integer k

# c.) INTUITION
# OPTION 1: using counting frequency and sorting
# We get the frequency of the number in the array and create a frequency dictionary using Counter.
# We then sort the list and get the k-1th position in the new sorted list, and that would represent the k most frequent elements

# OPTION 2: using Counter and bucket sort
# we sort the values using bucket sort technique
# Time complexity becomes O(n)

# d.) ALGORITHM
# OPTION 2
# 1. frequency_values = Counter(nums)
# 2. initialize bucket = [[] for _ in range(len(nums) + 1)]
# 3. top_frequency = 0
# 4. for item, frequency in frequency_values.items():
#       a.) bucket[frequency] = item
#       b.) top_frequency = max(top_frequency, frequency)
#
# 5. final_list = []
# 6. for index in reversed bucket range:
#       a.) if len(final_list) >= K: break
#       b.) if bucket[index] != "a": final_list.append(bucket[index])
# return final_list

# e.) COMPLEXITY
# Time: O(n): building the frequent for the values: O(n) + putting the items into their individual frequency bucket O(n) + O(n) getting the top k in the bucket index
# Space: O(n): storing the values and their frequency

# f.) EDGE CASES
# 1. nums list is empty: return the empty list
# 2. two numbers with same frequency: the bucket should be a list of list so as to store the same frequency values inside the list


from collections import Counter

def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    if len(nums) < 2: return nums
    
    frequency_values = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]
    top_frequency = 0

    for item, frequency in frequency_values.items():
        bucket[frequency].append(item)
        top_frequency = max(frequency, top_frequency)
    
    final_list = []

    for index in reversed(range(0, top_frequency + 1)):   
        if bucket[index]: 
            for value in bucket[index]:
                if len(final_list) >= k: return final_list
                final_list.append(value)

    return final_list
