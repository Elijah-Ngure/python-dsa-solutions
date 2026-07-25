# Pattern: Sliding Window 

## What It Is 
The sliding window technique maintains a contiguous subarray or substring of dynamic or
fixed size as it moves across the input. Instead of recomputing from scratch at each position, 
we add the new element entering the window and remove the element leaving it. 
This converts an O(n²) brute-force approach into O(n). 

## When to Use It 

- Finding the longest/shortest subarray or substring satisfying a condition (e.g. no repeating characters, sum ≤ target)
- Any problem asking about a contiguous section of an array/string
- Keywords in the problem: "subarray", "substring", "contiguous", "at most k", "longest", "minimum length"

## The Core Template 

```python 
left = 0
window_state = {} # or Counter, or int
for right in range(len(s)):
    # 1. Expand: add s[right] to window
    window_state[s[right]] = window_state.get(s[right], 0) + 1

    # 2. Shrink: if window violates condition, move left forward
    while [window violates condition]:
        window_state[s[left]] -= 1
        if window_state[s[left]] == 0:
            del window_state[s[left]]
        left += 1

    # 3. Update answer
    best = max(best, right - left + 1)
```
## Problems in This Folder 
| File | Problem | Key variation | 
|------|---------|---------------| 
| longest_substring_without_repeating.py | LC #3 | Variable window, char uniqueness | 
|minimum_size_subarray_sum.py | LC #209 | Variable window, sum condition | 
| find_all_anagrams_in_string.py | LC #438 | Fixed window, char frequency match | 

## Common Mistakes 

- Forgetting to shrink the window when the condition is violated
- Using a new array instead of maintaining state incrementally
- Off-by-one on window size calculation (`right - left + 1`) 
