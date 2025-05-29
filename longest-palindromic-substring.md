# 🔁 Longest Palindromic Substring – LeetCode Problem

I tried to solve the problem [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/) using **Python 3**.

---

## 🚀 Problem Explanation

You are given a string `s`, and you need to find the **longest substring** in it that is a **palindrome**—that is, it reads the same forwards and backwards.

- **Input:** A string `s` (up to 1000 characters).
- **Output:** The longest palindromic substring. If multiple exist, return any one.

---

## 💡 Idea – Brute Force: Try All Substrings

The basic approach is:
1. Generate all possible substrings.
2. Check if each one is a palindrome.
3. Track and return the longest one.

---

## 🧠 Code Description

- Initialize an empty string `chars` to store the longest palindrome found.
- Use two nested loops to generate all substrings of `s`:
  - Outer loop (`i1`) sets the **start index**.
  - Inner loop (`i2`) sets the **end index**.
- For each substring `s[i1:i2+1]`, check if it's equal to its reverse (`s[i1:i2+1][::-1]`).
- If it's a palindrome and longer than `chars`, update `chars`.
- Return the longest palindrome after checking all substrings.

---

## 🧑‍💻 Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        chars = ''
        for i1 in range(len(s)):
            for i2 in range(i1, len(s)+1):
                if s[i1:i2+1] == s[i1:i2+1][::-1] and i2-i1+1 > len(chars):
                    chars = s[i1:i2+1]
        return chars
```

---

## ✅ What's Good

- Very simple and easy to understand

- Works well for short strings

- No extra libraries needed



---

## ⚠️ What's Not Ideal

- Extremely inefficient for long strings

- Time Complexity: O(n³) — generating substrings + reversing them

- Not suitable for large-scale input


---

## 🔗 My Code on GitHub
You can check out the full code here:  
[👉 longest-palindromic-substring.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/longest-palindromic-substring.py)
