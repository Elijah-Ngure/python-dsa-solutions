# Pattern: Hash Maps & Sets

## What It Is

A hash map (Python `dict`) stores key-value pairs with O(1) average
lookup, insertion, and deletion. A hash set (Python `set`) stores
unique values with O(1) membership testing.

This is the single most important pattern in the entire collection.
Roughly 40% of Easy-Medium LeetCode problems have an optimal solution
that uses a hash map or set. If you feel stuck on a problem, ask
yourself: "Would storing something in a hash map help here?"

---

## When to Use Hash Map / Set

**Use a hash map when:**
- You need to count frequencies of elements
- You need to check if a complement/pair exists (Two Sum pattern)
- You need to group elements by a computed key (Group Anagrams)
- You need to remember where something was seen (index tracking)
- You need to detect a pattern across two structures

**Use a hash set when:**
- You only need to know IF something exists (not where or how many)
- You need to remove duplicates
- You need fast membership testing in a loop

**The core trade-off:** Hash maps trade **space** (O(n) extra memory)
for **time** (O(1) per lookup instead of O(n) linear search).
Always mention this trade-off explicitly in complexity analysis.

---

## Core Python Tools

```python
from collections import Counter, defaultdict

# --- Basic dict operations ---
freq = {}
freq["a"] = freq.get("a", 0) + 1   # safe increment without KeyError

# --- Counter: frequency map in one line ---
from collections import Counter
freq = Counter("mississippi")        # {'i': 4, 's': 4, 'p': 2, 'm': 1}
freq = Counter([1, 1, 2, 3, 3, 3])  # {3: 3, 1: 2, 2: 1}
freq.most_common(2)                  # [(3, 3), (1, 2)] — top 2 elements

# --- defaultdict: never raises KeyError ---
from collections import defaultdict
groups = defaultdict(list)
groups["key"].append("value")        # no need to check if key exists first

# --- Set operations ---
seen = set()
seen.add(3)
3 in seen           # O(1) — True
seen.discard(3)     # removes if present, no error if absent

# --- Checking and storing in one pattern (Two Sum style) ---
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:          # O(1) lookup
        return [seen[complement], i]
    seen[num] = i                   # store AFTER checking (avoid self-match)
```

---

## The Core Template: Frequency Counting

```python
from collections import Counter

def frequency_solution(data):
    freq = Counter(data)      # build frequency map: O(n) time, O(k) space

    for key, count in freq.items():
        # process each unique element and its count
        ...
```

---

## The Core Template: Grouping by Key

```python
from collections import defaultdict

def grouping_solution(items):
    groups = defaultdict(list)

    for item in items:
        key = compute_key(item)   # e.g. tuple(sorted(item)) for anagrams
        groups[key].append(item)

    return list(groups.values())
```

---

## Complexity Reference

| Operation | Average Time | Worst Case | Notes |
|-----------|-------------|-----------|-------|
| `d[key]` lookup | O(1) | O(n) | Worst case: hash collision (rare) |
| `d[key] = val` insert | O(1) | O(n) | Same as above |
| `key in d` membership | O(1) | O(n) | Fast in practice |
| `del d[key]` delete | O(1) | O(n) | |
| Build Counter(n items) | O(n) | O(n) | |
| `set.add()` | O(1) | O(n) | |
| `val in set` | O(1) | O(n) | Vs O(n) for list |

Space is always O(k) where k = number of unique keys (at most n).

---

## Problems in This Folder

| File | LeetCode # | Difficulty | Key technique |
|------|-----------|-----------|--------------|
| first_unique_character.py | #387 | Easy | Counter + scan for count == 1 |
| group_anagrams.py | #49 | Medium | defaultdict + sorted tuple as key |
| top_k_frequent_elements.py | #347 | Medium | Counter + heapq.nlargest |
| encode_decode_strings.py | #271 | Medium | Dict-based serialisation |
| valid_anagram.py | #242 | Easy | Counter comparison |

---

## Common Mistakes to Spot in AI-Generated Code

1. **Using a list for membership testing instead of a set:**
   ```python
   # BAD — O(n) per lookup, O(n²) overall
   seen = []
   if num in seen: ...

   # GOOD — O(1) per lookup
   seen = set()
   if num in seen: ...
   ```

2. **Forgetting `.get()` and causing a KeyError:**
   ```python
   # BAD — crashes if key doesn't exist
   freq[char] += 1

   # GOOD
   freq[char] = freq.get(char, 0) + 1
   # OR use defaultdict(int) which handles this automatically
   ```

3. **Checking after inserting in complement-style problems:**
   ```python
   # BAD — matches a number with itself (e.g. target=6, num=3)
   seen[num] = i
   if complement in seen: return ...   # finds num itself!

   # GOOD — check THEN store
   if complement in seen: return ...
   seen[num] = i
   ```

---

## Common Edge Cases

1. **Empty input** — Counter of empty list is `Counter()`, not an error
2. **All identical elements** — one key with count n
3. **Single element** — map has one entry; handle "top k" when k >= unique count
4. **Unicode / mixed case** — normalise with `.lower()` before hashing if needed
