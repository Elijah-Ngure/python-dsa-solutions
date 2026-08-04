# a.) PROBLEM
# LeetCode: #435: Non-overlapping intervals
# Difficulty: Medium
# Pattern: greedy, sorting, array
# Link: https://leetcode.com/problems/non-overlapping-intervals/

# b.) PROBLEM STATEMENT
# Given an array of intervals containing interval values [start, end], find the least number of intervals you'll have to remove from the list to ensure the list doesn't have any non-overlapping intervals

# c.) INTUITION
# We first sort the list of intervals by their end, this will put the overlapping intervals side by side (adjacent to each other.)
# This ensures that long-spanning intervals are at the end side of the list and short spanning intervals are the start side of the list.
# The algorithm then focuses on a greedy removal technique which removes the longer-spanning intervals that overlap with their previous short span intervals.
# The key idea is that (longer-spanning intervals cover a larger interval base which overlap with many other intervals compared to shorter spanning intervals, hence we pick these longer-spanning intervals to remove them.)
# we can then iterate the list selecting the first item, using it as the base interval, then remove all upcoming intervals that overlap with this one.
# once we get to one that doesn't overlap, we replace the base interval with this one, then we repeat the steps for greedily removing the upcoming intervals.

# d.) ALGORITHM
# 1. removals = 0
# 2. intervals.sort(key=lambda x:x[1]) sorting by the end value
# 3. base_interval = intervals[0]
# 4. intervals_length = len(intervals)
# 5. current_index = 1
# 6. while current_index < intervals_length:
#       a.) if base_interval[1] > intervals[current_index][0]:
#           i.) removals += 1
#       b.) Else:
#           i.) base_interval = intervals[current_index]
#       c.) current_index += 1
#
# 7. return removals

# e.) COMPLEXITY
# Time: O(n log n): sorting the intervals array: O(n log n) + iterating the list of intervals: O(n)
# Space: O(1): storing the pointer for the base_interval, current_index and interval_length

# f.) EDGE CASES
# 1. intervals list contains duplicates intervals: remove all other duplicates from the list.


def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    removals = 0
    intervals.sort(key=lambda x:x[1])
    base_interval = intervals[0]
    intervals_length = len(intervals)
    current_index = 1

    while current_index < intervals_length:
        # greedily remove the upcoming intervals that overlap with the base_interval
        
        if base_interval[1] > intervals[current_index][0]:
            removals += 1

        else:
            # select the next base interval
            base_interval = intervals[current_index]
        
        current_index += 1
    
    return removals
        
