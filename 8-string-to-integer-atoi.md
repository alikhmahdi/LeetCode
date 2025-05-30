# 🔢 String to Integer (atoi) – LeetCode Problem

I tried to solve the problem [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/description/) using **Python 3**.

---

## 🚀 Problem Explanation

The **String to Integer (atoi)** problem asks you to:

- Ignore leading whitespace.  
- Accept an optional '+' or '-' sign.  
- Read in digits until a non-digit is found.  
- Clamp the result within the 32-bit signed integer range: [−2³¹, 2³¹ − 1].  
- Return 0 if no valid conversion can be performed.

---

## 💡 Idea – Manual Parsing with Basic Conditions

The basic approach is to check the characters one by one and track the number, sign, and boundaries manually.

---

## 🧠 Code Description

### Initialization:

- `end` tracks if parsing has started.
- `num` is a list of valid digit characters.
- `chars` is a list of allowed non-digit characters (`+`, `-`, and space).
- `negtive` tracks if the number is negative.
- `r` accumulates the integer value.

### Parsing Logic:

- Loop through each character in the string `s`.
- Stop parsing if you hit a non-digit and non-sign/space after parsing started.
- If `-` is found first, mark the number as negative.
- If a digit is found, update the result.
- Once a number starts, ignore further non-digit characters.

### Result Logic:

- Clamp the result within 32-bit signed integer range:
  - If negative and within range → return `-r`
  - If negative and out of range → return `-2**31`
  - If positive and within range → return `r`
  - If positive and out of range → return `2**31 - 1`

---

## 🧑‍💻 Code

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        end = False
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chars = ['+', '-', ' ']
        negtive = False
        r = 0
        for c in s:
            if not c in num and not c in chars:
                break
            elif not end and c == '-':
                negtive = True
                end = True
            elif end and c in chars:
                break
            elif not end and c in ['-', '+']:
                end = True
            elif c in num:
                r = r*10 + int(c)
                end = True
        if negtive and r < 2**31:
            return -r
        elif negtive:
            return -2**31
        elif r < 2**31:
            return r
        else:
            return (2**31) - 1
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
[👉 string-to-integer-atoi.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/8-string-to-integer-atoi.py)
