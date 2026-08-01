# a.) PROBLEM
# LeetCode: #20: Valid Parentheses
# Difficulty: Easy
# Pattern: string, stack
# Link: https://leetcode.com/problems/valid-parentheses/

# b.) PROBLEM STATEMENT
# Given a string containing a mixture of the characters: "(", ")", "{", "}", "[", "]", determine if input string is valid.
# validity means that:
# i.) every oppening vracket has to have its constituent closing bracket of the same type later in the string or after it and
# ii.)  every closing bracket should have an openning bracket of the same type before it or ealier in the string and  
# iii.) open brackets must be closed in the correct order

# c.) INTUITION
# We use a stack to store the openning brackets (ensuring the latest opened bracket is at the top of the stack).
# for every closing bracket encountered, we pop the stack and compare it to check if they are of similar type. (If they are not or the stack if empty, the string is invalid)
# After completing iteration of the string, the stack should also be empty, if not, it means that there was an extra openning bracket that didn't have its resultant cosing bracket thus making the string invalid

# d.) ALGORITHM
# 1. stack = deque()
# 2. for element in s:
#   a.) if element in {"(", "{", "["}:
#       i.) stack.append(element)
#   b.) elif not stack:
#       i.) return False
#   c.) elif element == ")" and stack.pop() != "(":
#       i.) return False
#   d.) elif element == "}" and stack.pop() != "{":
#       i.) return False
#   e.) elif element == "]" and stack.pop() != "[":
#       i.) return False
#
# 3. return len(stack) == 0

# e.) Complexity
# Time: O(n): we iterate the string once
# Space: O(n): worst case when storing all elements are open brackets in the stack

# f.) EDGE CASES
# 1. All elements are openning brackets: we check the stack if it is empty and return False if its length is greater than zero.
# 2. String contains a closing bracket without an opening one: We check the stack if it has any elements before poping the value to compare the bracket. (if it is empty, we return False)

from collections import deque

def isValid(self, s: str) -> bool:
    
    stack = deque()
    
    for element in s:
        # add to the stack if it is a oppener
        if element in {"[", "{", "("}:
            stack.append(element)
        elif not stack:
            return False
        elif element == ")" and stack.pop() != "(":
            return False
        elif element == "}" and stack.pop() != "{":
            return False
        elif element == "]" and stack.pop() != "[":
            return False
    
    return len(stack) == 0
