# 🔢 Palindrome Number – LeetCode Problem

I tried to solve the problem [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/) using **Python 3**.

---

## 🚀 Problem Explanation

The **Palindrome Number** problem asks you to:

- Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

An integer is a palindrome when it reads the same backward as forward.  
For example: `121` is a palindrome, while `123` is not.  
Negative numbers are not palindromes (e.g., `-121` is not a palindrome).  
You can solve it without converting the integer to a string, but string conversion is allowed for a simple solution.

---

## 💡 Idea – Two Simple String-Based Approaches

I explored two solutions:
1. Compare characters one by one using indexing.
2. Use Python's list reversal trick to compare the full sequence.

---

## 🧠 Code Description – Method 1: Character-by-Character Check

- Convert the integer `x` to a string.
- Loop through the first half of the string.
- Compare each character from the start and the end.
- If any pair doesn't match, return `False`.
- Otherwise, return `True`.

### 🔍 Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        r = True
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                r = False
                break
        return r
```

---

## ✅ What's Good

- ✅ Simple logic with direct comparison  
- ✅ Easy to understand  
- ✅ No external libraries needed  

---

## ⚠️ What's Not Ideal?

- ❌ Slightly more verbose  
- ❌ Loops through multiple characters manually  

---

## 🧠 Code Description – Method 2: List Comparison

- Convert the number to a string and then to a list of characters.  
- Compare the list to its reversed version.  
- Return `True` if both match.  

---

## 🔍 Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        return x == x[::-1]
```

---

## ✅ What's Good

- ✅ Very short and clean  
- ✅ Easy to read  
- ✅ Fast and efficient  

---

## ⚠️ What's Not Ideal

- ❌ Still relies on string and list conversion  

---

## 🔗 My Code on GitHub

You can check out the full code here:  
[👉 palindrome-number.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/9-palindrome-number.py)
