# a.) PROBLEM
# LeetCode: #394: Decode String
# Difficulty: Medium
# Pattern: string, recursion
# Link: https://leetcode.com/problems/decode-string/

# b.) PROBLEM STATEMENT
# Given an encoded string, return the decoded string where the encoded string is encoded by a function k[encoded_string] such that decoded string = encoded_string repeated k times. 
# encoded_string could be a recursively encoded string where k[l[encoded_string]], where k and l are positive integers.

# c.) INTUITION
# We loop through the list, recursively multiplying the inner values of the brackets [] that have been decoded with the outer integer value.
# We will use a string variable for the temp_string at each level of the recursive function, another one for building the string's multiplier number{temp_number} (since we will be traversing the string and we could traverse a double or triple number i.e. 27[x] or 123[x]) and we'll use the temp_number to build the whole number for multiplying the inner decoded string.
# Each number formed is added to temp_number to build it.
# Each alphabet in the sequence is added to the current recursive function's temp_string.
# Each openning bracket "[" means a opening a new recursive function for decoding its inner values.
# Each closing bracket "]" means returning the current opened recursive function's decoded string to the function that called it earlier.

# d.) ALGORITHM
# 1. intialize index = 0
# 2. def decodeInner():
#       a.) nonlocal index 
#       b.) temp_number=""
#       c.) temp_string=""
#
#       d.) while index < len(s):
#           i.) if s[index].isdecimal(): 
#               1.) temp_number += s[index]
#               2.) index += 1
#
#           ii.) elif s[index] == "[": start recursion
#               1.) index += 1
#               2.) if temp_number:
#                       -temp_string += decodeInner() * int(temp_number)
#                        -reset temp_number = ""
#                    else: temp_string += decodeInner()
#
#           iii.) elif s[index].isalpha():
#                   1.) add to temp_string (temp_string += s[index])
#                   2.) index += 1
#
#           iv.) elif s[index] == "]": end recursion for this function
#                   1.) index += 1
#                   2.) return temp_string
#
#       e.) return temp_string
#
# 4.) return decodeInner()

# e.) COMPLEXITY
# 1. Time: O(n): looping through the values of the list once
# 2. Space: O(n): recursively decoding the list n times for nested inner values.

# f.) EDGE CASES
# 1. string has starting bracket without previous integer value: we check if the temp_number has a valid value before multiplying the recursive function with it.
# 2. number with multiple place values i.e. 23: we store the number in a temp_number variable, then convert the whole string number to a int before multipying the inner values of the brackets.

def decodeString(self, s: str) -> str:

    index = 0
           
    def decodeInner():
        nonlocal index
        
        temp_number = ""
        temp_string = ""

        while index < len(s):

            if s[index].isdecimal():
                # add to temp number
                temp_number += s[index]
                # advance index
                index += 1

            elif s[index] == "[":
                # advance index
                index += 1
                # call the recursive function
                if temp_number:
                    temp_string += (decodeInner() * int(temp_number))
                    temp_number = ""

                else:
                    temp_string += decodeInner()
            
            elif s[index].isalpha():
                temp_string += s[index]
                # advance index
                index += 1
            
            elif s[index] == "]":
                # advance the index
                index += 1
                # return the temporary string value
                return temp_string
        
        # return the temporary string value
        return temp_string

    return decodeInner()
        
