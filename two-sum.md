# Well, Well...

I tried to solve the problem [Two Sum](https://leetcode.com/problems/two-sum/description/) using *Python 3*.

## Let's Start

**Intuition:**  
The idea is to check every possible pair of numbers in the list to see if they add up to the target. I had two ideas for this.

---

## First Idea – Check by Members

We use two loops:  
- The first loop picks the first number.
- The second loop picks the next number after the first.
- If their sum equals the target, we return their indices.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1 in nums:
            for num2 in nums[nums.index(num1)+1:]:
                if target == num1 + num2:
                    return [nums.index(num1), nums.index(num2)]
```

### ❗ Problem  
If the input list is `[3, 3]` and the target is `6`, this returns `[0, 0]` instead of `[0, 1]`.  
The issue is with `nums.index(num2)`: when both numbers are the same, `.index()` always returns the first occurrence.  
I tried using `nums[::-1].index(num2)`, but that counts from the end and can still be confusing.

---

## Second Idea – Check by Index

This method avoids the `.index()` issue by working directly with indices.

We use two loops:  
- The first loop iterates over the first index.
- The second loop starts from the next index.
- If their sum equals the target, we return their indices.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if target == nums[index1] + nums[index2]:
                    return [index1, index2]
```

✅ This approach solves the duplicate-value problem because we already have the correct indices.

---

You can find my test and submitted code here:  
[🔗 two-sum.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/two-sum.py)
