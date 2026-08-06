# Pattern: Sliding Window

## What It Is

The sliding window technique maintains a contiguous subarray or
substring of dynamic or fixed size as it "slides" across the input.
Instead of recomputing results from scratch at each position, we
update our running state by adding the new element entering the
window on the right and removing the element leaving it on the left.

This converts an O(n²) brute-force approach (check every subarray)
into a single O(n) pass.

There are two variants:

**Fixed-size window:** The window length k is given. Slide it one
position at a time, adding the new right element and dropping the
old left element. Used for: max sum of k elements, anagram detection.

**Variable-size window:** The window grows and shrinks based on a
condition. Expand by moving right; shrink by moving left when the
condition is violated. Used for: longest substring without repeating
characters, smallest subarray with sum ≥ target.

---

## When to Use Sliding Window

- The problem asks about a **contiguous** subarray or substring
- You need the **longest** or **shortest** window satisfying a condition
- The problem has a sum, count, or character-frequency constraint
  that you need to maintain across positions
- Keywords: "subarray", "substring", "contiguous", "at most k
  distinct", "longest", "minimum length", "window"

**Red flag — do NOT use sliding window if:**
- The problem allows non-contiguous elements (use DP or greedy)
- The window condition can be violated then re-satisfied by shrinking
  from the right instead of the left (rare edge case)

---

## Core Templates

### Template A — Variable-size window (most common)

```python
from collections import defaultdict

def variable_window(s: str, condition_param) -> int:
    left = 0
    window_state = defaultdict(int)  # tracks content of current window
    best = 0

    for right in range(len(s)):
        # 1. EXPAND: add the new right element into the window
        window_state[s[right]] += 1

        # 2. SHRINK: while window violates the condition, move left forward
        while window_is_invalid(window_state, condition_param):
            window_state[s[left]] -= 1
            if window_state[s[left]] == 0:
                del window_state[s[left]]   # clean up zero entries
            left += 1

        # 3. UPDATE ANSWER: window is now valid — record if it's the best
        best = max(best, right - left + 1)

    return best
```

### Template B — Fixed-size window

```python
def fixed_window(nums: list, k: int) -> list:
    # Build the first window
    window_sum = sum(nums[:k])
    results = [window_sum]

    # Slide: add new right element, drop old left element
    for i in range(k, len(nums)):
        window_sum += nums[i]        # new element enters on the right
        window_sum -= nums[i - k]    # old element leaves on the left
        results.append(window_sum)

    return results
```

---

## The Window Size Formula

Inside any sliding window loop, the current window spans indices
`[left, right]` inclusive. Its size is:

```python
current_size = right - left + 1
```

The `+ 1` is required because both endpoints are included.
This is one of the most common off-by-one errors in AI-generated
sliding window code — check for it in every code evaluation task.

---

## Why the `>= left` Check Matters

In the longest-substring problem, we store the last-seen index of
each character. When we encounter a duplicate, we check:

```python
if char in char_index and char_index[char] >= left:
    left = char_index[char] + 1
```

The `>= left` condition prevents us from incorrectly shrinking the
window for a character we saw before the current window started
(a "stale" entry in the map). Without it, the left pointer could
jump backward, which breaks the algorithm entirely.

This subtle condition is a frequent omission in AI-generated
solutions — spotting it demonstrates genuine understanding.

---

## Complexity Reference

| Variant | Time | Space | Notes |
|---------|------|-------|-------|
| Fixed window | O(n) | O(1) | No state map needed for simple sums |
| Variable window (char map) | O(n) | O(k) | k = unique chars in window |
| Variable window (int sum) | O(n) | O(1) | State is a single integer |

Even though there is a `while` loop inside the `for` loop, each
element is added to and removed from the window at most once — so
the total operations are 2n → O(n). Make sure to explain this in
complexity justifications; reviewers expect you to address the
apparent O(n²) and explain why it is actually O(n).

---

## Problems in This Folder

| File | LeetCode # | Difficulty | Variant | Key condition |
|------|-----------|-----------|--------|---------------|
| longest_substring_without_repeating.py | #3 | Medium | Variable | No repeated char in window |
| minimum_size_subarray_sum.py | #209 | Medium | Variable | Sum ≥ target |
| find_all_anagrams_in_string.py | #438 | Medium | Fixed (len p) | Char frequencies match |

---

## Common Mistakes to Spot in AI-Generated Code

1. **Off-by-one in window size:**
   ```python
   # BUG — misses the rightmost element
   size = right - left

   # CORRECT
   size = right - left + 1
   ```

2. **Not cleaning up zero-count entries from the state map:**
   ```python
   # BUG — zero entries pollute the map; condition checks become wrong
   window_state[s[left]] -= 1
   left += 1

   # CORRECT — remove the key entirely when count reaches zero
   window_state[s[left]] -= 1
   if window_state[s[left]] == 0:
       del window_state[s[left]]
   left += 1
   ```

3. **Shrinking from the wrong side:**
   Sliding windows always shrink from the LEFT. An AI sometimes
   generates code that tries to shrink from the right, which
   destroys the contiguity guarantee of the window.

4. **Missing the `>= left` stale-entry guard** (see section above).

---

## Common Edge Cases

1. **Empty string / array** — loop never runs; return 0 or `[]`
2. **All identical characters** (`"bbbbb"`) — window stays size 1
3. **No repeats at all** (`"abcde"`) — window never shrinks; answer is full length
4. **Target sum larger than total array sum** — variable window never satisfies; return 0
5. **k larger than array length** — fixed window: validate k ≤ len(nums) first
