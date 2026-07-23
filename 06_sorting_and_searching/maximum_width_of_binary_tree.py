# a.) PROBLEM
# LeetCode: #662: Maximum Width of Binary Tree
# Difficulty: Medium
# Pattern: Binary Tree, Breadth-First Search
# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/

# b.) PROBLEM STATEMENT
# Given a root of a binary tree, get the largest width in the tree where the start_node and the end_node of the width are non-null
# width is the length between the end-nodes (leftmost and rightmost) non-null nodes

# c.) INTUITION
# Use Breadth-First Search to compute the width at each level of the tree.
# Since there will be some null nodes in tree, the most sure way to get the 
# index (number of the node in the tree) is to use the 
# formula left_node_index = parent_node_index * 2 and
# right_node_index = (parent_node_index * 2) + 1
# With the node indexes, we can correctly get the width of the non-null 
# endpoints by simply using their indexes (right_most_node_index - left_most_node_index)
# We store a variable for largest_width, each time updating it with the 
#computed width of the tree at each level only updating it only if it is larger than the current largest_width.
# i.e. largest_width = max(largest_width, computed_width)

# d.) ALGORITHM
# 1. set up a current_nodes list of nodes tuples (index, node) (non-null nodes) representing the current nodes at the current depth of the tree. (Initialize it with the root node)
# 2. Initialize the largest_width variable to 0
# 3. while current_nodes is not null:
#    a.) get the width of the current_nodes (right_most_node_index - left_most_node_index)
#    b.) set the largest_width: max(largest_width, width of current_nodes)
#    c.) Get the child nodes of the current_nodes in the list and replace the curren_nodes with the child nodes
# 4. return the largest_width

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# e.) COMPLEXITY
# Time: O(n) -> traversing the tree (breadth by breadth)
# Space: O(n) -> worst case for storing the nodes of a tree at each level breadth

# f.) EDGE CASES
# 1. no nodes provided: the largest_width is 0
# 2. null nodes in between the leftmost and rightmost nodes at each level: we use node index to mark the position of an index which is independent of other nodes. Node index is only dependent on its parent node's index

def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    largest_width = 0
    current_nodes = [(1, root)]

    while current_nodes:
        # count the width of the current level
        width = self.count_level_width(current_nodes)

        largest_width = max(largest_width, width)
        # Go deeper into the tree till the last level
        current_nodes = self.extract_child_nodes(current_nodes)
    
    return largest_width

def count_level_width(self, current_nodes_list):
    # get the left most node index
    left_index, node = current_nodes_list[0]
    # get the right most node index
    right_index, node = current_nodes_list[-1]
    # subtract the indexes of first and last non-nulls
    width = (right_index - left_index) + 1
    return width


def extract_child_nodes(self, current_nodes_list):
    child_nodes_list = []
    for index, node in current_nodes_list:
        if node.left is not None:
            # compute the index of the node
            left_node_index = index * 2
            # add the left node in the list
            child_nodes_list.append((left_node_index, node.left))
        if node.right is not None:
             # compute the index of the node
            right_node_index = (index * 2) + 1
            # add the right node in the list
            child_nodes_list.append((right_node_index, node.right))
    
    return child_nodes_list
