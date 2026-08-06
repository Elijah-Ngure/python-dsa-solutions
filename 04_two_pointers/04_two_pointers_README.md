# Pattern: Two Pointers

## What It Is

The two-pointer technique uses two index variables that move through
a data structure — typically from opposite ends, or at different speeds.
By coordinating their movement, we avoid the nested loops that a brute
force approach would require, reducing O(n²) to O(n).

There are two distinct variants:

**Variant A — Converging pointers:** Start one pointer at the left
end and one at the right end. Move them toward each other based on
a condition. Used for: palindrome checks, pair-sum in sorted arrays,
container problems.

**Variant B — Fast/slow pointers (Floyd's):** Both start at the same
position but move at different speeds. Used for: cycle detection in
linked lists, finding the middle of a list.

---

## When to Use Two Pointers

- The input array or string is **sorted** (or you can sort it first)
- You need to find a **pair or triplet** that satisfies a condition
- You need to check or build something from both ends simultaneously
- You need to detect a **cycle** in a linked list
- Keywords: "sorted array", "palindrome", "pair with sum", "remove
  duplicates in-place", "reverse in-place", "cycle"

---

## Core Templates

### Template A — Converging (sorted array, palindrome)

```python
def two_pointer_converging(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]   # or: check palindrome, etc.

        if current == target:
            return [left, right]           # found
        elif current < target:
            left += 1                      # need larger sum → move left right
        else:
            right -= 1                     # need smaller sum → move right left

    return []   # no solution found
```

### Template B — Fast / Slow (cycle detection)

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # moves 1 step
        fast = fast.next.next   # moves 2 steps

        if slow == fast:        # they meet → cycle exists
            return True

    return False                # fast reached end → no cycle
```

### Template C — Write pointer (remove duplicates in-place)

```python
def remove_duplicates(nums):
    write = 1   # position to write the next unique value

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:   # new unique value found
            nums[write] = nums[read]        # write it to the next slot
            write += 1

    return write   # new length
```

---

## Why Two Pointers Beats Brute Force

For a pair-sum problem on a sorted array:

```python
# BRUTE FORCE — O(n²): check every pair
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            return [i, j]

# TWO POINTERS — O(n): each pointer moves at most n steps total
left, right = 0, len(arr) - 1
while left < right:
    s = arr[left] + arr[right]
    if s == target: return [left, right]
    elif s < target: left += 1
    else: right -= 1
```

The key insight: because the array is sorted, moving left right
always increases the sum, and moving right left always decreases it.
This eliminates the need to check combinations we can reason away.

---

## Complexity Reference

| Problem type | Time | Space | Notes |
|-------------|------|-------|-------|
| Pair sum (sorted array) | O(n) | O(1) | No extra data structure |
| Palindrome check | O(n) | O(1) | Compare chars from both ends |
| Remove duplicates in-place | O(n) | O(1) | Write pointer technique |
| 3Sum | O(n²) | O(1) | Sort once O(n log n), then two-pointer per element |
| Cycle detection | O(n) | O(1) | Fast/slow meet at most after n steps |

Two-pointer solutions are prized because they are usually O(1) space —
no hash map, no auxiliary array. Mention this explicitly in complexity notes.

---

## Problems in This Folder

| File | LeetCode # | Difficulty | Variant |
|------|-----------|-----------|--------|
| valid_palindrome.py | #125 | Easy | Converging — compare from both ends |
| merge_sorted_array.py | #88 | Easy | Write pointer from the back |
| move_zeroes.py | #283 | Easy | Write pointer (keep non-zeros) |
| three_sum.py | #15 | Medium | Sort + converging per element |
| container_with_most_water.py | #11 | Medium | Converging — greedy move shorter side |

---

## Common Mistakes to Spot in AI-Generated Code

1. **Wrong pointer movement direction:**
   ```python
   # BUG: moves left when sum is too large (should move right)
   if current > target:
       left += 1   # wrong — increases the sum further

   # CORRECT
   if current > target:
       right -= 1  # decreases the sum
   ```

2. **Using `left < right` vs `left <= right`:**
   - Use `left < right` when you need two DISTINCT elements
   - Use `left <= right` for binary search (different pattern)
   - Mixing these up is a very common AI error

3. **Not sorting first for 3Sum:**
   ```python
   # BUG: two-pointer only works on sorted input
   for i in range(len(nums)):
       left, right = i+1, len(nums)-1
       ...  # will give wrong results if nums is unsorted

   # CORRECT
   nums.sort()   # must come before the loop
   for i in range(len(nums)):
       ...
   ```

4. **Not skipping duplicates in 3Sum:**
   After finding a valid triplet, advance pointers past duplicates
   to avoid adding the same triplet multiple times to the result.

---

## Common Edge Cases

1. **Empty or single-element input** — return early
2. **All same elements** — `[0, 0, 0]` for 3Sum should return `[[0,0,0]]`
3. **No valid pair/triplet** — return `[]` not `None`
4. **Negative numbers** — sorted order still works; moving pointers
   is still valid because sorted(-3, -1, 0, 2) behaves consistently
