# a.) PROBLEM
# LeetCode: #238: Product of Array Except Self
# Difficulty: Medium
# Pattern: array, prefix sum
# Link: https://leetcode.com/problems/product-of-array-except-self/

# b.) PROBLEM STATEMENT
# Given an array of numbers; nums, return an array answer such that each value in the list: answer[i] is equal to the product of all the other elements in the list except itself nums[i]

# c.) INTUITION
# we use prefix product and suffix product which will replace the integers with their corresponding prefix product * suffix product where we have two variables prefix_product and suffix_product and create a final list; answer.
# we then loop over the list twice: first to replace the numbers with their prefix product and store their prefix product in the final list.
# Second we loop over the list backwards to multiply each number's prefix product with its suffix product to ensure that for each number in the nums list i.e. nums[i] is replaced with its prefix product and suffix product.

# d.) ALGORITHM
# 1. prefix_product = 1
# 2. final_list = [0] * len(nums)
# 3. for index, value in enumerate(nums):
#       a.) final_list[index], prefix_product = prefix_product, value * prefix_product
# 4. suffix_product = 1
# 5. for index in reversed(range(len(nums))):
#       a.) final_list[index], suffix_product = final_list[index] * suffix_product, suffix_product * nums[index]
# 6. return final_list

# e.) COMPLEXITY
# Time: O(n): looping through the nums list twice for prefix and suffix product
# Space: O(n): storing the final_list for the answer

# f.) EDGE CASES
# 1. List contains zeros: using prefix and suffix sum eliminates division strategy hence no issue of dividing by zero errors


def productExceptSelf(self, nums: List[int]) -> List[int]:

    final_list = [0] * len(nums)
    prefix_product = 1

    # prefix product
    for index, value in enumerate(nums):
        final_list[index], prefix_product = prefix_product, (prefix_product * value)
    
    # reset the product so far
    suffix_product = 1

    # suffix product
    for index in reversed(range(len(nums))):
        final_list[index], suffix_product = (final_list[index] * suffix_product), (suffix_product * nums[index])

    return final_list
