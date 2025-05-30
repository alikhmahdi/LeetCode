
# 🔠 Median of Two Sorted Arrays – LeetCode Problem

I tried to solve the problem [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/) using **Python 3**.

---

## 🚀 Problem Explanation

You are given two **sorted arrays** `nums1` and `nums2`.  
You need to return the **median** of the two sorted arrays.

- The median is the middle value in an ordered list of numbers.
- If the number of elements is even, the median is the average of the two middle values.

---

## 💡 Idea – Brute Force Merge and Sort

The basic approach is to:
1. Combine both arrays into a single one.
2. Sort the combined array.
3. Return the median based on the total number of elements.

---

## 🧠 Code Description

- Combine `nums1` and `nums2` into a list called `nums`.
- Sort `nums` to make sure all elements are in order.
- Check the total length:
  - If **odd**, return the middle element.
  - If **even**, return the **average** of the two middle elements.
- Convert the result to a float (since median is expected to be a float).

---

## 🧑‍💻 Code

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 != 0:
            return float(nums[len(nums) // 2])
        else:
            return float((nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2)
```

---

## ✅ What's Good

- Simple and easy to understand
- Useful for small input sizes
- No extra libraries required

---

## ⚠️ What's Not Ideal

- Not optimal for large datasets

---

## 🔗 My Code on GitHub

You can check out the full code here:  
[👉 median-of-two-sorted-arrays.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/median-of-two-sorted-arrays.py)
