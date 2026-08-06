# Pattern: Mixed Patterns

## What It Is

This folder contains problems that each introduce a distinct
algorithmic idea not covered in the other five pattern folders.
Rather than a single unified technique, these problems share one
thing: each requires you to think about the problem structure first
before reaching for a data structure or formula.

The patterns covered here are:

| Sub-pattern | Core idea |
|-------------|-----------|
| **Dynamic Programming (lite)** | Break into subproblems; reuse stored results |
| **Prefix Sums** | Pre-compute running totals for O(1) range queries |
| **Greedy** | Make the locally optimal choice at each step |
| **Prefix Products** | Pre-compute products excluding each position |

These are introduced at the "lite" level — foundational understanding,
not advanced DP or complex greedy proofs. That is appropriate for the
Easy-Medium tier and for AI training platform coding tracks.

---

## Sub-Pattern 1: Dynamic Programming (DP) — Lite

### What It Is

DP solves a problem by breaking it into overlapping subproblems,
solving each once, and storing the result so it is never recomputed.
The stored results are kept in a table (array or dictionary).

The two questions that define every DP problem:

1. **What is the subproblem?** — "What is the best way to reach
   position i?" or "What is the max profit up to day i?"
2. **How do later subproblems depend on earlier ones?** — This is
   called the **recurrence relation** and is the core of DP.

### The Simplest DP — Climbing Stairs

```
f(1) = 1   (one way to reach step 1: take one 1-step)
f(2) = 2   (two ways: 1+1 or 2)
f(n) = f(n-1) + f(n-2)   ← recurrence relation
```

This is exactly the Fibonacci sequence. Solved iteratively:

```python
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev2, prev1 = 1, 2   # f(1), f(2)

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
```

Time: O(n) · Space: O(1) — we only keep the last two values.

### House Robber — Classic State Transition

```
rob(i) = max(
    rob(i-1),           # skip house i (don't rob it)
    rob(i-2) + nums[i]  # rob house i (must skip i-1)
)
```

```python
def rob(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current

    return prev1
```

### Recognising DP Problems

Keywords: "maximum/minimum", "number of ways", "can you reach",
"optimal", "count distinct", "at most k steps". If the brute force
is exponential (trying every possibility) and subproblems repeat —
it is a DP problem.

---

## Sub-Pattern 2: Prefix Sums

### What It Is

A prefix sum array stores the running total up to each index.
Once built in O(n), it answers "what is the sum of elements from
index i to j?" in O(1) — without re-summing the range each time.

```python
nums    = [3,  1,  4,  1,  5,  9]
prefix  = [3,  4,  8,  9, 14, 23]   # prefix[i] = sum of nums[0..i]

# Sum from index 2 to 4 (inclusive):
# Without prefix: 4 + 1 + 5 = 10 (O(n) scan)
# With prefix:    prefix[4] - prefix[1] = 14 - 4 = 10 (O(1))
```

### The Template

```python
def build_prefix(nums: list) -> list:
    prefix = [0] * (len(nums) + 1)   # prefix[0] = 0 (sentinel)
    for i, val in enumerate(nums):
        prefix[i + 1] = prefix[i] + val
    return prefix

# Range sum query [left, right] (0-indexed, inclusive)
def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

The sentinel `prefix[0] = 0` means range queries from index 0
work without special-casing: `prefix[right+1] - prefix[0]`.

### Prefix Products — Product of Array Except Self

The same idea applied to multiplication instead of addition.
No division allowed → build a left-products array and a
right-products array, then combine them:

```python
def product_except_self(nums: list) -> list:
    n = len(nums)
    result = [1] * n

    # Left pass: result[i] = product of all elements to the LEFT of i
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Right pass: multiply in the product of all elements to the RIGHT
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result
```

Time: O(n) · Space: O(1) extra (output array doesn't count).

---

## Sub-Pattern 3: Greedy

### What It Is

A greedy algorithm makes the locally optimal choice at each step
without looking ahead, trusting that local optimality leads to
global optimality. When greedy works, it is elegant and fast.
When it doesn't work, you need DP instead.

Greedy works when the problem has the **greedy choice property**:
a locally optimal choice is always part of some globally optimal
solution. This must be true by the problem's structure — not assumed.

### Maximum Subarray — Kadane's Algorithm (Greedy)

At each position: extend the current subarray, OR start fresh
from here (whichever is larger).

```python
def max_subarray(nums: list) -> int:
    current = nums[0]    # current subarray sum ending at this position
    best = nums[0]       # best sum seen so far

    for num in nums[1:]:
        # Greedy choice: is it better to extend or restart?
        current = max(num, current + num)
        best = max(best, current)

    return best
```

The greedy choice: `max(num, current + num)` — if `current` is
negative, it drags down any extension, so it is better to start
fresh. This insight converts an O(n²) brute force into O(n).

### Non-Overlapping Intervals — Greedy Scheduling

Sort by **end time**, then greedily keep each interval that starts
at or after the previous one ends. Count how many you must remove.

```python
def erase_overlap_intervals(intervals: list) -> int:
    intervals.sort(key=lambda x: x[1])   # sort by end time
    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            last_end = end    # keep this interval
        else:
            count += 1        # remove it (overlaps with the one we kept)

    return count
```

**Why sort by end (not start):** We want to keep the interval that
ends earliest, leaving maximum room for future intervals. Sorting by
start would not give this guarantee.

---

## Complexity Reference

| Sub-pattern | Build time | Query time | Space |
|-------------|-----------|-----------|-------|
| DP (tabulation) | O(n) | — | O(n) or O(1) with optimisation |
| Prefix sum array | O(n) | O(1) per query | O(n) |
| Kadane's (greedy) | O(n) | — | O(1) |
| Greedy scheduling | O(n log n) sort + O(n) sweep | — | O(1) extra |
| Prefix products | O(n) two passes | — | O(1) extra |

---

## Problems in This Folder

| File | LeetCode # | Difficulty | Sub-pattern |
|------|-----------|-----------|------------|
| climbing_stairs.py | #70 | Easy | DP — Fibonacci recurrence |
| house_robber.py | #198 | Medium | DP — state transition |
| maximum_subarray.py | #53 | Medium | Greedy — Kadane's algorithm |
| product_of_array_except_self.py | #238 | Medium | Prefix products (two passes) |
| non_overlapping_intervals.py | #435 | Medium | Greedy — sort by end time |

---

## Common Mistakes to Spot in AI-Generated Code

### DP Mistakes

1. **Initialising DP with wrong base case:**
   ```python
   # BUG — dp[0] = 0 is wrong for House Robber with n=1
   dp = [0] * n
   dp[0] = 0   # should be nums[0]
   ```

2. **Wrong recurrence direction** (computing dp[i] using dp[i+1]
   when the recurrence goes forward, or vice versa):
   Always check: does dp[i] depend on smaller or larger indices?

3. **Using O(n) space when O(1) is possible:**
   Most 1D DP only needs the last 1–2 values. AI often stores
   the full array unnecessarily. Spot and mention this in reviews.

### Prefix Sum Mistakes

4. **Off-by-one in range query:**
   ```python
   # BUG — excludes right endpoint
   total = prefix[right] - prefix[left]

   # CORRECT (0-indexed, inclusive right)
   total = prefix[right + 1] - prefix[left]
   ```

5. **Not including a sentinel zero at index 0:**
   Without `prefix[0] = 0`, a query from index 0 requires a
   special case. The sentinel eliminates this.

### Greedy Mistakes

6. **Sorting by wrong key for interval problems:**
   ```python
   # BUG for non-overlapping intervals — sort by start, not end
   intervals.sort(key=lambda x: x[0])

   # CORRECT — sort by end time for scheduling/non-overlap problems
   intervals.sort(key=lambda x: x[1])
   ```

7. **Using greedy when the problem requires DP:**
   Greedy fails when a locally good choice blocks a globally better
   one. If test cases fail after a greedy approach, the problem
   likely needs DP. AI makes this mistake frequently on harder variants.

---

## Common Edge Cases

1. **All negative numbers (Maximum Subarray)** — Kadane's still works;
   answer is the least negative element (initialise with nums[0], not 0)
2. **Single element (Climbing Stairs, House Robber)** — handle before loop
3. **Two elements (House Robber)** — `max(nums[0], nums[1])`; no dp[i-2]
4. **Empty intervals list** — return 0 before any sorting
5. **All intervals overlap** — count = n-1 (keep only one)
6. **Product array with zeros** — prefix product approach handles naturally;
   note it in edge case comments because divide-based approaches fail here
