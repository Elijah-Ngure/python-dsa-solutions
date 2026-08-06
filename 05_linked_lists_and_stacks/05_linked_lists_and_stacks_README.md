# Pattern: Linked Lists & Stacks

## What It Is

### Linked Lists

A linked list is a sequence of nodes where each node holds a value
and a pointer to the next node. Unlike arrays, nodes are not stored
in contiguous memory — you can only reach a node by following
pointers from the head.

This makes some operations cheap (O(1) insert/delete at a known
node) and others expensive (O(n) access by index — no random access).

In Python, LeetCode problems provide a `ListNode` class:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

You never define this yourself in solutions — the problem provides it.
But you must understand it deeply to traverse and manipulate lists.

### Stacks

A stack is a Last-In, First-Out (LIFO) structure. The last element
added is the first one removed. In Python, a regular list used with
`.append()` and `.pop()` is a stack — both operations are O(1).

Stacks are ideal for problems involving:
- Matching/nesting (parentheses, brackets)
- "Undo" or backtrack to previous state
- Keeping track of elements in a specific order while processing

---

## When to Use Linked List Techniques

- The problem gives you a `ListNode` structure to work with
- You need to reverse, split, merge, or detect cycles in a sequence
- You need O(1) insertion/deletion without index-based access
- Keywords: "linked list", "node", "next pointer", "cycle", "reverse",
  "middle of list", "merge two lists"

## When to Use a Stack

- You need to process elements in reverse order of arrival
- You have opening/closing pairs to match (brackets, tags, quotes)
- You need to remember previous states while scanning forward
- Keywords: "valid parentheses", "matching brackets", "next greater
  element", "evaluate expression", "undo operations"

---

## Core Templates

### Linked List Traversal

```python
def traverse(head: ListNode):
    current = head
    while current:               # stops when current is None (end of list)
        process(current.val)
        current = current.next
```

### Reverse a Linked List (in-place, O(1) space)

```python
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        next_node = current.next    # 1. save next before we overwrite it
        current.next = prev         # 2. reverse the pointer
        prev = current              # 3. advance prev
        current = next_node         # 4. advance current

    return prev   # prev is now the new head (last node of original list)
```

The three-variable dance (`prev`, `current`, `next_node`) is
the canonical reversal pattern. Every linked list reversal
problem uses a variant of this structure.

### Fast / Slow Pointer (Cycle Detection — Floyd's Algorithm)

```python
def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # moves 1 step
        fast = fast.next.next     # moves 2 steps

        if slow == fast:          # they meet → cycle confirmed
            return True

    return False   # fast reached None → no cycle
```

**Why this works:** If there is a cycle, the fast pointer laps
the slow pointer inside the cycle. If there is no cycle, the fast
pointer reaches the end (None). They are guaranteed to meet after
at most n steps — O(n) time, O(1) space (no set needed).

### Stack — Valid Parentheses Pattern

```python
def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}  # closing → expected opening

    for char in s:
        if char in '({[':
            stack.append(char)          # push opening bracket
        else:
            if not stack or stack[-1] != pairs[char]:
                return False            # no matching opener
            stack.pop()                 # matched — remove opener

    return len(stack) == 0   # valid only if all openers were matched
```

---

## The Dummy Node Trick

Many linked list problems (merge, remove, insert) become much
cleaner with a dummy node at the head. It eliminates special
handling for the head and lets you return `dummy.next` at the end:

```python
dummy = ListNode(0)    # fake head node — val doesn't matter
dummy.next = head
current = dummy

# ... manipulate the list using current ...

return dummy.next      # the real head (may have changed)
```

Without dummy nodes, you often need ugly special cases for
"what if the head itself needs to be removed?" — avoid this.

---

## Complexity Reference

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Traverse full list | O(n) | O(1) | Follow next pointers |
| Reverse list (in-place) | O(n) | O(1) | Three-pointer dance |
| Detect cycle (Floyd's) | O(n) | O(1) | No set needed |
| Detect cycle (set method) | O(n) | O(n) | Simpler but costs space |
| Stack push / pop | O(1) | — | Python list `.append()` / `.pop()` |
| Stack `in` check | O(n) | — | Don't search stacks — use dict |

**Important for code reviews:** The cycle detection problem can be
solved naively with a `visited = set()` — O(n) space. The fast/slow
pointer solution is O(1) space. Always note this difference when
evaluating AI solutions.

---

## Problems in This Folder

| File | LeetCode # | Difficulty | Technique |
|------|-----------|-----------|----------|
| reverse_linked_list.py | #206 | Easy | Three-pointer reversal |
| linked_list_cycle.py | #141 | Easy | Fast/slow pointer (Floyd's) |
| valid_parentheses.py | #20 | Easy | Stack + closing-to-opening map |
| implement_stack_using_queues.py | #225 | Easy | Deque as stack |

---

## Common Mistakes to Spot in AI-Generated Code

1. **Losing the next pointer before overwriting it:**
   ```python
   # BUG — next_node is lost; list becomes broken
   current.next = prev
   current = current.next   # current.next is now prev, not the original next!

   # CORRECT — save next BEFORE overwriting
   next_node = current.next
   current.next = prev
   current = next_node
   ```

2. **Off-by-one in fast pointer check:**
   ```python
   # BUG — crashes with AttributeError if fast.next is None
   while fast:
       fast = fast.next.next   # fast.next might be None

   # CORRECT — check both fast AND fast.next
   while fast and fast.next:
       fast = fast.next.next
   ```

3. **Stack not checked before popping:**
   ```python
   # BUG — IndexError if stack is empty when closing bracket arrives
   if stack[-1] != pairs[char]:
       return False
   stack.pop()

   # CORRECT — check emptiness first
   if not stack or stack[-1] != pairs[char]:
       return False
   stack.pop()
   ```

4. **Forgetting to return `dummy.next` instead of `head`:**
   When using a dummy node, the original `head` reference is stale
   if the head was modified. Always return `dummy.next`.

---

## Common Edge Cases

1. **Empty list (`head = None`)** — return None or False immediately
2. **Single node** — reversal returns same node; cycle is impossible
3. **Two nodes** — fast/slow: fast reaches end in one step; check this
4. **Unmatched opening bracket at end** — stack not empty → return False
5. **Empty string for parentheses** — empty stack at end → return True
