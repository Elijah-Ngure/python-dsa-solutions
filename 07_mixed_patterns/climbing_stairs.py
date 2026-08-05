# a.) PROBLEM
# LeetCode: #70: Climbing Stairs
# Difficulty: Easy
# Pattern: fibonacci series, math
# Link: https://leetcode.com/problems/climbing-stairs/

# b.) PROBLEM STATEMENT
# suppose you are climbing a staircase which takes n steps to reach the top where you can either climb 1 or 2 steps with each stride up the stairs. In how many distinct ways can you climb the staircase to the top.
# This include the unique combination of 1 step and 2 steps to reach n

# c.) INTUITION
# Since we can climb the stairs in either one step or two steps. We can decide to add:
# i.) All the variations for climbing the stairs if I take the first stride as 1 step plust
# ii.) All the variations for climbing the stairs if I take the first stride as 2 steps.
# When I take my first stride as 1 step, the remaining steps to the top are n-1 which equal the number of all comibinations to get to the top when n is n-1
# When I take my first stride as 2 steps, the remeining steps to the top are n-2 which equal the number of all combinations to get to the top when n is n-2
# To simplify, steps for n stairs = steps for n-1 stairs + steps for n-2 stairs.
# since this pattern holds for all values of n > 2 and steps when n=1 is 1 and n=2 is 2, we can use these are the base sum for calculating the value of distinct ways to climb to the top for any n>2

# d.) ALGORITHM
# 1. previous1_steps = 2
# 2. previous2_steps = 1
# 3. if n == 1: return 1
# 4. elif n == 2: return 2
#
# 5. for stairs in range(3, n):
#       a.) previous2_steps, previous1_steps = previous2_steps, (previous2_steps + previous1_steps)
# return previous2_steps + previous1_steps

# e.) COMPLEXITY
# Time: O(n): traversing the n stairs once
# Space: O(1): storing the previous1_steps and previous2_steps numbers

# f.) EDGE CASES
# 1. When n is 1, there is no previous steps: so we just return the 1 step which is (1step)
# 2. When n is 2, there is no previous 2 steps: so we just return the 2 distinct steps for when n is 2 which is (1step + 1step) and (2steps)

def climbStairs(self, n: int) -> int:
    if n == 1: return 1
    elif n == 2: return 2

    previous1_steps = 2
    previous2_steps = 1

    for stairs in range(3, n):
        previous1_steps, previous2_steps = (previous2_steps + previous1_steps), previous1_steps
    
    return previous1_steps + previous2_steps
