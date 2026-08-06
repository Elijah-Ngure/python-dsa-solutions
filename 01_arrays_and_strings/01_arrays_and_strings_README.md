# Pattern: Arrays & Strings

## What It Is

Arrays and strings are the most fundamental data structures in
programming. Most problems in this category require you to iterate
through elements, track running state, or apply string-specific
methods to transform or analyse data.

These problems rarely require a fancy algorithm — they test whether
you write clean, readable Python and handle edge cases properly.
They are the baseline that every AI code evaluation task assumes
you can do fluently.

---

## When to Use Array / String Techniques

- The problem asks you to scan, count, or transform elements
- You need to track a running minimum, maximum, or sum
- The problem involves reversals, rotations, or rearrangements
- Keywords: "find", "count", "check if", "return the index of",
  "rotate", "reverse", "remove", "maximum/minimum value"

---

## Core Python Tools for This Pattern

```python
# Iteration with index
for i, val in enumerate(arr):
    ...

# Reverse a list or string
arr[::-1]               # creates new reversed list
arr.reverse()           # in-place, returns None
reversed_str = s[::-1]  # strings are immutable — creates new string

# Essential string methods
s.lower()               # lowercase — use before any char comparison
s.isalnum()             # True if alphanumeric (key for palindrome checks)
s.split()               # split on whitespace into list
" ".join(["a","b","c"]) # join list into string with separator
s.replace("a", "b")     # replace all occurrences

# Tracking a running best
best = float('-inf')    # initialise for maximum problems
best = float('inf')     # initialise for minimum problems
for val in arr:
    best = max(best, val)
```

---

## The Most Important Mistake to Spot

**String concatenation inside a loop — O(n²) hidden cost:**

```python
# BAD — O(n²): strings are immutable, each + creates an entirely new string
result = ""
for char in s:
    result = result + char   # <-- creates new string every iteration

# GOOD — O(n): collect in a list, join once at the end
parts = []
for char in s:
    parts.append(char)
result = "".join(parts)      # single O(n) operation
```

This is one of the most frequent bugs in AI-generated Python.
Spotting and explaining it is a core skill on Mindrift and Outlier
coding tracks — mention it explicitly in your evaluation justification.

---

## Complexity Reference

| Operation | Time | Notes |
|-----------|------|-------|
| Access by index `arr[i]` | O(1) | Direct memory address |
| Search unsorted list | O(n) | Must check every element |
| Append to list | O(1) amortised | Occasional resize is O(n) |
| Insert at index i | O(n) | Shifts all elements after i |
| Slice `arr[i:j]` | O(j-i) | Creates a new list |
| String concatenation `+` | O(n) per operation | Avoid in loops |
| `"".join(list)` | O(n) total | Always use this instead |
| `in` on list | O(n) | Linear scan |
| `in` on set | O(1) | Hash lookup |

---

## Problems in This Folder

| File | LeetCode # | Difficulty | Key technique |
|------|-----------|-----------|--------------|
| two_sum.py | #1 | Easy | Hash map complement lookup |
| valid_anagram.py | #242 | Easy | Character frequency (Counter) |
| contains_duplicate.py | #217 | Easy | Hash set membership |
| best_time_to_buy_sell_stock.py | #121 | Easy | Running minimum tracking |
| reverse_string.py | #344 | Easy | Two-pointer in-place swap |
| first_unique_character.py | #387 | Easy | Counter + linear scan |
| maximum_subarray.py | #53 | Medium | Kadane's algorithm |
| product_of_array_except_self.py | #238 | Medium | Prefix + suffix products |

---

## Common Edge Cases to Always Check

1. **Empty input** — `if not arr: return ...` before any logic
2. **Single element** — does your loop still produce the right answer?
3. **All identical elements** — `[3, 3, 3]` — does duplicate detection still work?
4. **Negative numbers** — initialise running min/max with `float('-inf')` not `0`
5. **String case sensitivity** — apply `.lower()` before any character comparison
