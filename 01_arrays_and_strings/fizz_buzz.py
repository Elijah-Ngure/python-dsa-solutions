# a.) PROBLEM
# LeetCode: #412: Fizz Buzz
# Difficulty: Easy
# Pattern: string
# Link: https://leetcode.com/problems/fizz-buzz/description/

# b.) PROBLEM STATEMENT
# Provided an integer n, return a string array upto the integer n, where the values of the string in the array is its position number or 
# i.) if the number in that position is divisible by 3 and 5: its value is "FizzBuzz"
# ii.) if it is divisible by 3: its value is "Fizz"
# iii.) if it is divisible by 5: its value is "Buzz"

# c.) Intuition
# We loop through the range of given integer (n), where for each value:
# we check if it divisible by 3 and 5, its string is "FizzBuzz" or
# if it is divisible by 3, its value is "Fizz" or 
# if it is divisible by 5, its value is "Buzz"

# d.) ALGORITHM
# 1. create a final list equal to the range(n)
# 2. Loop through the ranges i.e. for each index:
#    a.) Increment the index by 1 (since indexes start on 0)
#    b.) calculate the divisibility of the number by 3 and 5 respectively
#    c.) If it is divisible by both 3 and 5: final_list[index] = "FizzBuzz"
#    d.) If it is divisible by 3: final_list[index] = "Fizz"
#    e.) If it is divisible by 5: final_list[index] = "Buzz"
#    f.) Else; final_list[index] = str(number)
# 3. return the final_list

# e.) COMPLEXITY
# Time: O(n): creating the list of n values O(n) + looping through the range(n): O(n)
# Space: O(n): to hold the final list of string values

# f.) EDGE CASES
# 1. Number not divisible by either 3 or 5: store the number as a string


def fizzBuzz(self, n: int) -> List[str]:
    final_list = ["Fizz" for _ in range(n)]
    for index in range(n):
        number = index + 1
        # check if divisible by 3 and 5
        _3divisible = number % 3 == 0

        _5divisible = number % 5 == 0

        if _3divisible and _5divisible:
            final_list[index] = "FizzBuzz"
                        
        # check if is divisible by 3
        elif _3divisible:
            final_list[index] = "Fizz"

        # check if is divisible by 5
        elif _5divisible:
            final_list[index] = "Buzz"
        
        else:
            final_list[index] = str(number)
    
    return final_list
