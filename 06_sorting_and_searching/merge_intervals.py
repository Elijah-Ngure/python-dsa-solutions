# a.) PROBLEM
# LeetCode #56: Merge Intervals
# Difficulty: Medium
# Pattern: sort first, then linear sweep
# Link: https://leetcode.com/problems/merge-intervals/

# b.) PROBLEM STATEMENT
# Provided a list of intervals [start, end], merge all overlapping intervals
# and return a list of non-overlapping intervals that cover all input ranges.

# c.) INTUITION
# When we sort the list of inputs by their [start] value, we ensure that 
# the overlapping values are adjacent to each other. We can then traverse 
# the list just once: O(n) checking if the current inteval overlaps with the previous one. 
# An overlap occurs when the [start] value of an interval is <= (less than or 
# equal to) [end] value of the previous interval: [current_start <= previous_end]
# Merging: for the two overlapping intervals, we keep the previous_start and 
# get the maximum value between the two end values i.e. max(previous_end, current_end)

# d.) ALGORITHM
# 1. Sort the list of intervals by their [start] value
# 2. Create an output list to store the final non-overlapping intervals
# 3. For each interval [start, end]
#    if output list is empty --> we add the interval [start, end] in the list
#    elif the interval is merged with the recent entry in output list:
#       -->update the end value of output interval to max(end, ouput[-1][1])
#    else: There is no overlap, hence add the interval into the final output list

# e.) COMPLEXITY
# Time: O(n log n) --> sorting the list: O(log n) * linear traversing the list O(n)
# Space: O(n)  --> for storing the output list of values upto n (worst case).

# f.) EDGE CASES
# 1. single Interval -- loop only run once adding the interval into the output list
# 2. All intervals overlap -- merges to one interval (start i, end n-1)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key=lambda x: x[0])
        # Traverse the list 
        for period in intervals:
            if not output:
                output.append(period)
                continue
            
            if period[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], period[1])
            
            else:
                output.append(period)
        
        return output
        
