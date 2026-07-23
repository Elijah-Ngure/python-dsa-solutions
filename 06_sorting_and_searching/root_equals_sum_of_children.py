# a.) PROBLEM
# LeetCode: #2236: Root Equals Sum of Children
# Difficulty: Easy
# Pattern: Binary Tree (Search)
# Link: https://leetcode.com/problems/root-equals-sum-of-children/

# b.) PROBLEM STATEMENT
# Check the sum of children of a root of a binary tree to see if they are equal to the to its root. (Return True if this is the case, otherwise return False)

# c.) INTUITION
# Since there are only 3 nodes, I will just simply get the value of left_node 
# of the root and the value of the right_node of the root.
# I will then compare their sum to check if they equal the value of the root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# d.) ALGORITHM
# 1. Get the value of the right_node (root.right.val)
# 2. Get the value of the left_node (root.left.val)
# 3. a.) if sum of right_node and left_node equal root value (root.val): return True
#     b.) Else: return False

# e.) COMPLEXITY
# Time: O(1) -> we get the value of the right_node O(1) + 
#               we get the value of left_node O(1) +
#               comparing the sum of values to the root node O(1)
# Space: O(1) -> we store the left_node and right_node sum for comparison with root node value


def checkTree(self, root: Optional[TreeNode]) -> bool:
    left_and_right_sum =  root.left.val + root.right.val
    if left_and_right_sum == root.val:
        return True

    return False
