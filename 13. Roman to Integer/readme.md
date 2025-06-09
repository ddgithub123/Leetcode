# Leetcode Problem 13
# Roman to Integer

## Problem Statement

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written from **largest to smallest** from left to right. However, in some cases, smaller numbers appear before larger ones to indicate subtraction:

### Subtraction Rules:
- **I** before **V** (5) or **X** (10): 4 (`IV`), 9 (`IX`)
- **X** before **L** (50) or **C** (100): 40 (`XL`), 90 (`XC`)
- **C** before **D** (500) or **M** (1000): 400 (`CD`), 900 (`CM`)

Given a Roman numeral string `s`, convert it to an **integer**.

### Constraints
- 1 ≤ `s.length` ≤ 15  
- `s` contains only valid Roman numeral characters (`I`, `V`, `X`, `L`, `C`, `D`, `M`)
- `s` is a **valid** Roman numeral in the range `[1, 3999]`

---

## Examples

1. **Input:** `s = "III"`  
   **Output:** `3`  
   **Explanation:** `III = 3`

2. **Input:** `s = "LVIII"`  
   **Output:** `58`  
   **Explanation:** `L = 50, V = 5, III = 3`

3. **Input:** `s = "MCMXCIV"`  
   **Output:** `1994`  
   **Explanation:** `M = 1000, CM = 900, XC = 90, IV = 4`

---

## Complexity

- **Time Complexity:** O(n)  
  *(We iterate through each character once from right to left.)*

- **Space Complexity:** O(1)  
  *(Only a fixed-size dictionary and a few variables are used.)*

---
