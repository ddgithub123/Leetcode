# Leetcode Problem 159
# Longest Substring with At Most Two Distinct Characters

## Problem Statement

Given a string `s`, find the length of the **longest contiguous substring** that contains **at most two distinct characters**.

### Constraints
- 1 ≤ `s.length` ≤ 10⁵  
- `s` contains only English letters (uppercase or lowercase)

### Example
1. **Input:** `s = "eceba"`  
   **Output:** `3`  
   **Explanation:** `"ece"` has two distinct characters.

2. **Input:** `s = "ccaabbb"`  
   **Output:** `5`  
   **Explanation:** `"aabbb"` has two distinct characters.

3. **Input:** `s = "aaaaa"`  
   **Output:** `5`  
   **Explanation:** One unique character, entire string is valid.

---

## Test Cases

| # | Input           | Output | Explanation                           |
|---|------------------|--------|---------------------------------------|
| 1 | `"eceba"`        | `3`    | `"ece"` is valid                      |
| 2 | `"ccaabbb"`      | `5`    | `"aabbb"` is valid                    |
| 3 | `"aaaaa"`        | `5`    | All same character                    |
| 4 | `"a"`            | `1`    | Single character                      |
| 5 | `"abab"`         | `4`    | Entire string is valid                |
| 6 | `"abcde"`        | `2`    | Any pair like `"ab"`, `"bc"` is valid |
| 7 | `"aabbccaa"`     | `4`    | `"aabb"` or `"ccaa"` are valid        |
| 8 | `"a"*100000`     | `100000`| All same character                    |
| 9 | `"aAbBcC"`       | `2`    | Each pair has 2 distinct characters   |

---

## Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---
