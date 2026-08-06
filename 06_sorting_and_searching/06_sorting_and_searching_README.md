# Pattern: Sorting & Searching

## What It Is

### Sorting

Sorting rearranges elements into a defined order (usually ascending).
Its power in problem-solving comes not from the sorted output itself,
but from what sorting *enables*: once data is sorted, problems that
would otherwise require O(n²) pairwise comparisons can often be
solved in O(n) with a single linear scan or two-pointer sweep.

The key question to ask is: **"Would knowing the order of elements
help me solve this faster?"** If yes — sort first.

Python's built-in `sorted()` and `.sort()` both use Timsort:
O(n log n) time, O(n) space for `sorted()`, O(1) extra for `.sort()`.

### Binary Search

Binary search finds a target in a **sorted** array in O(log n) time
by repeatedly halving the search space. Each comparison eliminates
half the remaining candidates.

Binary search is also a general problem-solving strategy: any problem
where you can ask "is the answer ≥ some value?" in O(1) or O(n) time
can be solved with binary search on the answer space — even if no
explicit array is present.

---

## When to Use Sorting + Linear Sweep

- You need to find pairs or intervals that relate to each other
- The brute force is O(n²) comparisons → sorting + O(n) scan = O(n log n)
- Keywords: "merge overlapping intervals", "find all duplicates",
  "group together", "nearest", "non-overlapping"

## When to Use Binary Search

- The input array is **sorted** (or you can sort it)
- You need to find a specific value or its insertion position
- You need the k-th smallest/largest element efficiently
- Keywords: "sorted array", "find target", "search", "k-th element",
  "minimum/maximum that satisfies condition"

---

## Python Sorting — What You Must Know

```python
# sorted() — returns a NEW list, original unchanged
nums = [3, 1, 4, 1, 5]
result = sorted(nums)               # [1, 1, 3, 4, 5]
result = sorted(nums, reverse=True) # [5, 4, 3, 1, 1]

# .sort() — sorts IN-PLACE, returns None
nums.sort()                         # nums is now [1, 1, 3, 4, 5]
nums.sort(reverse=True)

# Custom sort key — sort by a computed value
intervals = [[3, 6], [1, 3], [2, 4]]
intervals.sort(key=lambda x: x[0])  # sort by start value → [[1,3],[2,4],[3,6]]

words = ["banana", "fig", "apple"]
words.sort(key=len)                  # sort by string length → ["fig","apple","banana"]

# Sort by multiple keys — tuple comparison
data.sort(key=lambda x: (x[0], -x[1]))  # ascending first, descending second
```

**Critical distinction for code reviews:**
```python
# BUG — .sort() returns None; result is None, not the sorted list
result = nums.sort()   # common AI mistake

# CORRECT
nums.sort()
result = nums          # or: result = sorted(nums)
```

---

## Binary Search Template

```python
def binary_search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1   # inclusive right boundary

    while left <= right:    # <= because both endpoints are valid candidates
        mid = left + (right - left) // 2   # avoids integer overflow vs (left+right)//2

        if nums[mid] == target:
            return mid          # found
        elif nums[mid] < target:
            left = mid + 1      # target is in the right half
        else:
            right = mid - 1     # target is in the left half

    return -1   # target not found
```

### The Three Pointer Variants — Know All Three

```python
# Standard: find exact target
left, right = 0, len(nums) - 1
while left <= right:
    ...

# Find leftmost position where condition is first True
left, right = 0, len(nums)   # right is len(nums), not len-1
while left < right:           # < not <=
    mid = (left + right) // 2
    if condition(mid):
        right = mid           # keep mid as candidate
    else:
        left = mid + 1

# Find rightmost position where condition is True
left, right = 0, len(nums) - 1
while left < right:
    mid = (left + right + 1) // 2  # +1 prevents infinite loop when left+1==right
    if condition(mid):
        left = mid
    else:
        right = mid - 1
```

---

## Merge Intervals — The Sort-First Pattern

```python
def merge(intervals: list) -> list:
    intervals.sort(key=lambda x: x[0])  # MUST sort by start first
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:                    # overlaps current
            merged[-1][1] = max(merged[-1][1], end)   # extend if needed
        else:
            merged.append([start, end])               # no overlap: new interval

    return merged
```

**Why sort first:** Overlapping intervals are only guaranteed to be
adjacent after sorting. Without sorting, you'd need O(n²) comparisons
to check every interval against every other one.

**Why `max()` on the end:** One interval can be fully contained inside
another (e.g. [1,10] and [2,5]). Without `max()`, you'd incorrectly
shrink the end to 5.

---

## Heap / Priority Queue for K-th Largest

```python
import heapq

def find_kth_largest(nums: list, k: int) -> int:
    # Method 1: Sort (O(n log n), simple)
    return sorted(nums, reverse=True)[k - 1]

    # Method 2: Min-heap of size k (O(n log k), better for large n)
    heap = nums[:k]
    heapq.heapify(heap)                    # build min-heap from first k elements

    for num in nums[k:]:
        if num > heap[0]:                  # larger than smallest in heap
            heapq.heapreplace(heap, num)   # replace smallest with new element

    return heap[0]   # smallest in the heap = k-th largest overall
```

Python's `heapq` is a **min-heap** — `heap[0]` is always the smallest.
For a max-heap, negate all values: `heapq.heappush(heap, -val)`.

---

## Complexity Reference

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Python `.sort()` / `sorted()` | O(n log n) | O(1) / O(n) | Timsort — stable |
| Binary search | O(log n) | O(1) | Requires sorted input |
| Merge intervals (after sort) | O(n) sweep | O(n) output | Dominated by sort |
| Build heap | O(n) | O(k) | `heapq.heapify()` |
| Heap push/pop | O(log k) | — | k = heap size |
| `nlargest(k, nums)` | O(n log k) | O(k) | Faster than full sort when k << n |

---

## Problems in This Folder

| File | LeetCode # | Difficulty | Key technique |
|------|-----------|-----------|--------------|
| merge_intervals.py | #56 | Medium | Sort by start + linear sweep |
| binary_search.py | #704 | Easy | Standard binary search template |
| search_in_rotated_sorted_array.py | #33 | Medium | Modified binary search |
| kth_largest_element.py | #215 | Medium | Min-heap of size k |
| non_overlapping_intervals.py | #435 | Medium | Greedy — sort by end, count removals |

---

## Common Mistakes to Spot in AI-Generated Code

1. **Binary search off-by-one (the most common bug):**
   ```python
   # BUG — misses the last element; right should be len-1
   right = len(nums)

   # BUG — infinite loop when left and right are adjacent
   mid = (left + right) // 2
   left = mid    # if condition is False and left==mid, left never advances

   # CORRECT — always use mid+1 or mid-1 to advance
   left = mid + 1
   right = mid - 1
   ```

2. **Assigning the return of `.sort()` to a variable:**
   ```python
   # BUG — result is None
   result = intervals.sort(key=lambda x: x[0])

   # CORRECT
   intervals.sort(key=lambda x: x[0])
   result = intervals
   ```

3. **Not using `max()` when merging intervals:**
   ```python
   # BUG — fails when one interval is fully inside another [1,10] + [2,5]
   merged[-1][1] = end

   # CORRECT
   merged[-1][1] = max(merged[-1][1], end)
   ```

4. **Python `heapq` is a min-heap, not max-heap:**
   ```python
   # BUG — heapq gives minimum, not maximum
   heapq.heappush(heap, val)
   print(heap[0])   # this is the SMALLEST, not largest

   # CORRECT for max-heap — negate values
   heapq.heappush(heap, -val)
   print(-heap[0])  # negate back to get true value
   ```

---

## Common Edge Cases

1. **Single interval** — merge returns it unchanged
2. **All intervals overlap** — merge returns one interval
3. **Target not in array** — binary search returns -1
4. **Duplicate elements** — binary search: which occurrence to return?
5. **k == len(nums)** — k-th largest is the minimum element
6. **Touching intervals [1,4] and [4,6]** — 4 ≤ 4 → should merge to [1,6]
