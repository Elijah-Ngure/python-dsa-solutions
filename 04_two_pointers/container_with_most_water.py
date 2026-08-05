# a.) PROBLEM
# LeetCode: #11: Container With Most Water
# Difficulty: Medium
# Pattern: two pointers, prefix sum
# Link: https://leetcode.com/problems/container-with-most-water/

# b.) PROBLEM STATEMENT
# Given an array of n integers that depict different heights which correspond to n vertical lines drawn such that the ith vertical line is (i, height[i]), find two lines (i1 and i2) such that together with the x-axis, they form a container that contains the most water (area).
# The height of the container cannot be slant and will have to be min(height[i1], height[i2])

# c.) INTUITION
# Knowing that if all the lines were equal, the maximum area would be gotten by the edge lines (first and last indexes in the array), we will start calculating the area from the edge lines going inside.
# The inputs doesn't guarantee the largest area will be formed by the outer lines, so we'll have to test different candidates for the largest area that can be filled with water.
# We will have a prefix variable to hold the largest area so far.
# We will iterate the array using the two pointers, calculating the area formed by the two lines then updating the prefix area if it is larger than previous stored one.
# Area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1) which will be the width
# We will move inwards by dropping the smaller of the two current heights.
# The idea is that, there might be two lines that are long that they may form the largest are due to their vertical height or combination of both vertical height and width (x-distance which is the difference in their index)

# d.) ALGORITHM
# 1. largest_area = 0
# 2. pointer1 = 0
# 3. pointer2 = len(height) - 1
# 4. while pointer1 < pointer2:
#       a.) min_height = min(height[pointer1], height[pointer2])
#       b.) width = pointer2 - pointer1
#       c.) area = min_height - width
#       c.) largest_area = max(largest_area, area)
#       d.) if height[pointer1] == min_height:
#           i.) pointer1 += 1
#       e.) Else:
#           i.) pointer1 -= 1
#
# 5. return largest_area

# e.) COMPLEXITY
# Time: O(n): traversing the heights using two pointers that will loop through the elements once.
# Space: O(1): storing the pointer1, pointer2 and the largest_area variables.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_area = 0
        pointer1 = 0
        pointer2 = len(height) - 1

        while pointer1 < pointer2:
            min_height = min(height[pointer1], height[pointer2])
            width = pointer2 - pointer1
            area = min_height * width
            largest_area = max(largest_area, area)

            # move the pointer with the lesser height
            if height[pointer1] == min_height:
                pointer1 += 1
            else:
                pointer2 -= 1

        return largest_area
