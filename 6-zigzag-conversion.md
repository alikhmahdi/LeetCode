
# 🔀 Zigzag Conversion – LeetCode Problem

I tried to solve the problem [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/description/) using **Python 3**.

---

## 🚀 Problem Explanation

The **Zigzag Conversion** problem asks you to rearrange a string `s` into a zigzag pattern on a given number of rows (`numRows`), and then read the pattern row by row to create a new string.

---

## 💡 Idea – Simulate the Zigzag Pattern

The basic approach is:
- Use a list of strings (one for each row).
- Determine where each character in the string belongs using a zigzag index pattern.
- After assigning all characters, concatenate all rows to form the final string.

---

## 🧠 Code Description

**Initialization:**
- Create a list `r` of empty strings, one for each row.

**Character Placement:**
- Loop through each character in the input string `s`.
- Use a zigzag pattern formula to determine its correct row.

**Zigzag Logic:**
- If `numRows > 1`, calculate:
  ```python
  n = i % ((numRows * 2) - 2)
  ```
- If `numRows == 1`, just place all characters in the first row.

**Row Assignment:**
- If `n < numRows`, it's part of the downward zig.
- Else, it's part of the upward zag, and we place it using:
  ```python
  r[-(n - numRows) - 2]
  ```

**Final Result:**
- Join all rows together to form the final zigzag string.

---

## 🧑‍💻 Code

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = ['' for _ in range(numRows)]
        for i in range(len(s)):
            if numRows > 1:
                n = i % ((numRows * 2) - 2)
            else:
                n = 0
            if n < numRows:
                r[n] += s[i]
            else:
                r[-(n - numRows) - 2] += s[i]
        return ''.join(r)
```

---

## ✅ What's Good

- ✅ Easy to implement and understand  
- ✅ Handles both short and long inputs well  
- ✅ No external libraries required

---

## ⚠️ What's Not Ideal

- ❌ Not the most optimized approach in terms of space (stores all rows explicitly)
- ❌ Still a bit tricky to grasp the zigzag indexing math

---

## 🔗 My Code on GitHub

You can check out the full code here:  
[👉 zigzag-conversion.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/zigzag-conversion.py)
