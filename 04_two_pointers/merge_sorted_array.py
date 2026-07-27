# a.) PROBLEM
# LeetCode: #88: Merge Sorted Array
# Difficulty: Easy
# Pattern: array, sorting, two pointers
# Link: https://leetcode.com/problems/merge-sorted-array/

# b.) PROBLEM STATEMENT
# Given two integer arrays; nums1 and nums2 sorted in an ascending order, and two integers m an n, representing the number of elements in the arrays respectively, merge the second array: nums2 onto the first array nums1 ensuring the whole merged array is in an ascending order.
# The first array: nums1 has a combined length that can fit the second array in it. The positions for the second array in the nums1 are fitted with zeros indicating they need to be replaced by the elements from nums2

# c.) INTUITION
# Since both arrays are sorted in an ascending order, and the nums1 array contains placeholders for values in nums2, we start arranging the elements in nums1 list from the largest to the smallest (using values from both arrays where we select the biggest value as we traverse the two lists backwards)
# When nums1 list is exhausted before the second list: nums2, we simply replace the values in the remaining index with the values remaining in nums2.
# When the second list: nums2 is exhausted, it means the arrangement of values in nums1 are correctly in ascending order.

# d.) ALGORITHM
# 1. initialize pointer1 (original_pointer) = m - 1
# 2. initialize pointer2 (substiture_pointer) = n - 1
# 3. get the full length of nums1: full_length = len(nums1)
# 4. if n < 1: return (nums2 is empty)
# 5. for index in reversed(range(full_length)):
#       a.) if pointer2 < 0: (remaining index values in nums1 are already sorted correctly)
#           i.) break;
#       b.) if pointer1 < 0: (we have exhausted the original numbers in nums1, so we replace the remaining indexes with values from nums2)
#          i.) nums1[index] = nums2[pointer2]
#          ii.) pointer2 -= 1
#       c.) elif nums1[pointer1] > nums2[pointer2]:
#          i.) nums1[index] = nums1[pointer1]
#          ii.) pointer1 -= 1
#       d.) else:
#           i.) nums1[index] = nums2[pointer2]
#           ii.) pointer2 -= 1

# e.) COMPLEXITY
# Time: O(m + n): we traverse the two lists n and m
# Space: O(1): we update the first list in place

# f.) EDGE CASES
# 1. nums2 values are all lesser than the current values in nums1: the pointer1 becomes less than 0, we update the remaining indexes of the nums1 list with the values from nums2
# 2. nums2 values are exhausted: the remaining values in nums1 list are correctly sorted. 

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    substitute_pointer = n-1
    original_pointer = m-1

    for index in reversed(range(0, len(nums1))):
            if substitute_pointer < 0:
                break
            
            if original_pointer < 0:
                nums1[index] = nums2[substitute_pointer]
                substitute_pointer -= 1

            elif nums1[original_pointer] > nums2[substitute_pointer]:
                nums1[index] = nums1[original_pointer]
                original_pointer -= 1

            else:
                nums1[index] = nums2[substitute_pointer]
                substitute_pointer -= 1
        
