
# 🔠 Longest Substring Without Repeating Characters – LeetCode Problem

I tried to solve the problem [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) using **Python 3**.

---

## 🚀 Problem Explanation

Given a string `s`, you need to find the length of the **longest substring** that contains **no repeating characters**.

- A **substring** is a contiguous sequence of characters within the string.
- All characters in the substring must be **unique**.

---

## 💡 Idea – Brute Force Search

The approach is to **start a new substring from every character** in the string and keep extending it **until a character repeats**. While doing so, we keep track of the maximum length found.

---

## 🧠 Code Description

- `r` keeps track of the **maximum length** found.
- **Outer loop** (`for i in range(len(s))`) starts a new substring from each character.
- **Inner loop** (`for i1 in range(i, len(s))`) extends the substring as long as there are no repeated characters.

### 🧪 Logic Breakdown:

- `l` is a list that stores characters in the current substring.
- `realize` counts the length of the current substring.
- If the character is **not in** `l`, we add it and increase `realize`.
- If it's **already in** `l`, we break the inner loop.
- After each inner loop, update `r` if the current `realize` is greater.

---

## 🧑‍💻 Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            l = []
            realize = 0
            for i1 in range(i, len(s)):
                if not (s[i1] in l):
                    realize += 1
                    l.append(s[i1])
                else:
                    break
            if r < realize:
                r = realize
        return r
```

---

## ✅ What's Good

- Easy to understand and implement
- Works correctly for small inputs

---

## ⚠️ What's Not Ideal

- **Inefficient** for large strings (O(n²) time complexity)
- Can be optimized using sliding window + set

---

## 🔗 My Code on GitHub

You can check out the full code here:  
[👉 longest-substring-without-repeating-characters.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/3-longest-substring-without-repeating-characters.py)
