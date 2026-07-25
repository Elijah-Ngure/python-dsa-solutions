# a.) PROBLEM
# LeetCode: #2095: Delete the Middle of a Linked List
# Difficulty: Medium
# Pattern: Linked List, Two pointers
# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# b.) PROBLEM STATEMENT
# Provided the head of a linked list, delete the middle node (n // 2)th and return the head.

# c.) INTUITION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# OPTION 1: We can add the linked list values into a list, get the node just before the middle node (len(list) // 2) - 1 [if it exists]. set the link of that node (self.next) to link to the node after the middle node [if it exist] i.e. self.next = self.next.next

# OPTION 2: A better approach will be to use the idea that "a middle node is halfway to the end of the last node in the tree".
# With the idea, we maintain three pointers (end, middle and the previous_middle pointer).
# We traverse through the tree, each iteration moving the middle and previous_middle pointer one step forward, and move the end pointer two points ahead.
# With that when we reach the end of the tree (the end.next pointer is None), it means that the middle node is at the middle of the tree.
# This option runs in O(n) but runs only n/2 times compared to the Option 1 which is O(n) and runs n times.
# After reaching the middle node, we simple set the previous_middle next pointer to the node after the middle node. i.e. previous_middle.next = middle.next

# d.) ALGORITHM
# 1. Initiate the pointers: previous_middle, middle, end = head
# 2. while end.next and end.next.next:
#   a.) move the end pointer two points ahead: end = end.next.next
#   b.) move the previous_middle pointer one point ahead: previous_middle = middle
#   c.) move the middle_pointer one point ahead: middle_pointer = middle_pointer.next
# 3. if the tree had two middle nodes (end.next exists):
#   a.) move the previous_middle pointer one point ahead: previous_middle = middle
# 4. remove the link of the middle node: previous_middle.next = middle.next
# 5. return the head

# e.) COMPLEXITY
# Time: O(n): running the faster pointer (end) and slow pointer (middle) takes n/2 times
# Space: O(1): storing the three pointers (end, middle, previous_middle)

# f.) EDGE CASES
# 1. only one node in the tree: return None (remove the head node)
# 2. Tree has two middle nodes: select the second middle node to remove (move the previous_middle node one node forward)


def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # have three points
    previous_middle = head
    middle = head
    end = head

    if head.next is None:
        return None
    
    while end.next and end.next.next:
        # update the pointers
        end = end.next.next
        previous_middle = middle
        middle = middle.next
    
    # move the middle forward for double middle values
    if end.next: 
        previous_middle = middle
        middle = middle.next
    # delete the middle item
    # point the next from the previous middle to the next of the middle item
    previous_middle.next = middle.next

    return head
