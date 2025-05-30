# 🔁 Reverse Integer – LeetCode Problem

I tried to solve the problem [Reverse Integer](https://leetcode.com/problems/reverse-integer/description/) using **Python 3**.

---

## 🚀 Problem Explanation

The **Reverse Integer** problem asks you to reverse the digits of an integer `x`.  
If the reversed integer overflows a 32-bit signed integer range (from -2³¹ to 2³¹ - 1), return `0`.

---

## 💡 Idea – Reverse with Simple String Operations

The basic idea is:
- Convert the integer to a string (ignore the negative sign temporarily).
- Reverse the digits.
- Restore the negative sign if needed.
- Check if the result is within the 32-bit signed integer range.

---

## 🧠 Code Description

**Check sign:**  
- If `x` is negative, make it positive temporarily, reverse, and then restore the negative sign.

**Reverse digits:**  
- Use Python string slicing to reverse the digits.

**Overflow check:**  
- If the reversed number is not in the 32-bit signed integer range, return `0`.

---

## 🧑‍💻 Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            r = int(''.join([n for n in str(x)][::-1]))
        else:
            x = -x
            r = int(''.join([n for n in str(x)][::-1]))
            r = -r
        if -2**31-1 < r < 2**31-1:
            return r
        else:
            return 0
```

---

## ✅ What's Good

- ✅ Easy to implement and understand  
- ✅ Handles both positive and negative integers  
- ✅ No external libraries needed

---

## ⚠️ What's Not Ideal?

- ❌ Not optimized for performance-critical environments  
- ❌ Uses string manipulation instead of pure mathematical operations

---

## 🔗 My Code on GitHub

You can check out the full code here:  
[👉 reverse-integer.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/7-reverse-integer.py)
