# a.) PROBLEM
# LeetCode: #2130: Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Pattern: Linked List, Two pointers, array
# Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# b.) PROBLEM STATEMENT
# Given the head of a singly-linked list with even length, return the maxiumum twin sum of the linked list where;
# Twin are nodes that their indexes are equidistant from each other from either side (counting from left side or right side)

# c.) INTUITION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# OPTION 1: We use two pointers (faster and slow pointer to get the middle node), where the end node (faster pointer) moves twice as much as the middle node (slow pointer).
# The idea is that the end node is twice the distance of the middle node.
# After getting the middle node, we reverse the second part of the tree (reversing their pointers), so that now the two parts of the tree are separate and each of their positions is a twin of the other in the other part of the tree.
# We loop through the two tree simultaneously getting the twin sum, updating the final sum if it is greater than the current final sum.
# its time complexit is O(n) = getting the middle O(n/2) + reversing the pointers O(n/2) + getting the twin sum O(n/2)

# OPTION 2: We use a list, which is more intuitive, we store the nodes' values into a list.
# We then traverse the list upto the middle element, each iteration getting the node at that index and the node equidistant from the other side (its twin).
# calculate the sum of the two, then update the final sum if they exceed it
# Its time complexity is O(n) = putting the nodes in a list O(n) + summing the twins O(n/2). 
# At the hardware level, getting values from a contingent array list is faster than getting it from node objects.
# Using a list uses additional storage O(n) compare to O(1) for option 1

# OPTION 3: Using a stack
# We use the two pointers method(fast and slow pointer) and add the first half of the nodes' values into a stack,
# Then we continue traversing the second half of the tree, getting the twin sum (popping the stack, getting the node.val of the next node).
# We begin summing the twins from the middle going outwards.
# Its time complexity is O(n): O(n/2) first half of nodes in a stack + O(n/2) traversing second half doing the sum of the twins

# d.) ALGORITHM
# 1. create a stack to hold the nodes' values
# 2. create two pointers (middle = head and end = head.next)
# 2. while end.next and end.next.next:
#   a.) end = end.next.next
#   a.) values_list.push(middle.val)
#   b.) middle = middle.next
# 3. Get the len of stack n_len = len(values_list)
# 4. Initialize max_sum = 0
# 5. Continue from the next portion of the tree
# 6. while middle:
#   a.) first_twin = values_list.pop()
#   a.) second_twin = middle.val
#   c.) middle = middle.next
#   c.) max_sum = max(max_sum, (first_twin + second_twin))
# 6. return max_sum

# e.) COMPLEXITY
# Time: O(n): putting the first half of nodes' values in a stack O(n/2) + summing the twins O(n/2). 
# Space: O(n): storing the first half of nodes' values: O(n/2)

# f.) EDGE CASES
# 1. Even number of nodes: The constraint is a list of even interger from n = 2 onwards
# 2. Only two nodes in the list: we add the first node value in the stack list before the while loop 


from collections import deque


def pairSum(self, head: Optional[ListNode]) -> int:
    values_list = deque()
    middle = head
    values_list.append(middle.val)
    end = head.next

    # if we are not at the middle go deeper into the list
    while end.next and end.next.next:
        # update the end and middle values
        middle = middle.next
        end = end.next.next
        values_list.append(middle.val)
        
    
    # Getting the twin sum
    current = middle.next
    final_sum = 0

    while current:
        first_twin = values_list.pop()
        second_twin = current.val
        final_sum = max(final_sum, (first_twin + second_twin))
        current = current.next
    
    return final_sum
