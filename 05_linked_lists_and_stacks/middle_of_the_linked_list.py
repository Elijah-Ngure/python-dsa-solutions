# a.) PROBLEM
# LeetCode: #876: Middle of the Linked List
# Difficulty: Easy
# Pattern: Linked list
# Link: https://leetcode.com/problems/middle-of-the-linked-list/

# b.) PROBLEM STATEMENT
# Provided the head of a singly linked list, return the middle node of that tree. (return the furthest most middle node if two share the middle position)

# c.) INTUITION
# since singly-linked list are not indexed, we will have to put them in a list and get the count of them all.
# After putting them in a list, we get the middle node by getting the middle index of the list (middle_index = len(list) // 2) and return the node at that particular position

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# d.) ALGORITHM
# 1. initialize a list with the head of the tree
# 2. get the child_node of the current head
# 3. while child_node is not None:
#   a.) append the child_node into the list
#   b.) get the child_node of the current child_node
# 4. get the middle index of the list: middle = (len(list) // 2)
# 5. return the node at that position: list[middle]

# e.) COMPLEXITY
# Time: O(n): traversing through the tree and adding the items into the list
# Space: O(n): storing the list of nodes

# f.) EDGE CASES
# 1. The tree has only one item (the head): floor division (len(list) // 2) always returns a valid index, so 1 // 2 = 0, which is the valid index for the node in the list


def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    values_list = [head]
    next_node = head.next
    # index the items
    while next_node is not None:
        values_list.append(next_node)
        next_node = next_node.next

    # get the middle of the items
    middle_index = (len(values_list) // 2)
    
    return values_list[middle_index]
