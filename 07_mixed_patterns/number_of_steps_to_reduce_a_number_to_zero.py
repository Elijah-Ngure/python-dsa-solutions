# a.) PROBLEM
# LeetCode: #1342: Number of Steps to Reduce a Number to Zero
# Difficulty: Easy
# Pattern: bit manipulation
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# b.) PROBLEM STATEMENT
# Given an integer num, return the number of steps to reduce it to zero, where you can only use two operations i.e. divide it by 2 when it is even or subtract 1 from it when it is odd

# c.) INTUITION
# we divide the number by 2 when it is even or subtracting 1 from it when it is odd, repeating this process until the number becomes zero, each iteration incrementing the steps that was taken

# d.) ALGORITHM
# 1. initialize the steps to 0
# 2. While num > 0:
#   a.) if num is even: divide it by 2
#   b.) If num is odd: subtract one from it
#   c.) increment steps

# e.) COMPLEXITY
# Time: O(log n): where n is the num value
# Space: O(1): for storing the steps: O(1)

# f.) EDGE CASES
# 1. num provided is zero: we return the initialized steps (0)



def numberOfSteps(self, num: int) -> int:
    steps = 0
    while num > 0:
        # check if it is even
        if num % 2 == 0:
            num = num / 2
        # it is odd
        else:
            num -= 1

        steps += 1
    
    return steps
