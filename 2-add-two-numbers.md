
# ➕ Add Two Numbers – LeetCode Problem

I tried to solve the problem [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/) using **Python 3**.

---

## 🚀 Problem Explanation

You are given two non-empty linked lists that represent two non-negative integers.  
- The digits are stored in **reverse order**.  
- Each node contains a **single digit**.  
- You need to add the two numbers and return the **sum** as a linked list.

> 📚 If you're not familiar with linked lists, [check out this explanation](https://github.com/alikhmahdi/LeetCode/blob/main/linked-list.md).

---

## 💡 First Idea – Convert to Python Lists

Let’s admit it — solving this with regular Python lists is way easier 😅

---

### 🔧 Function 1 – Convert Linked List to Python List

This function walks through the linked list and stores the values in a regular list.

```python
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
```

---

### 🔁 Function 2 – Build Linked List from List

This takes a Python list and creates a linked list from it.

```python
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
```

---

### 🧠 Main Logic

This approach converts the two linked lists into numbers, adds them, and builds a new linked list from the result.

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = linked_list_to_list(l1)
        l2 = linked_list_to_list(l2)
        l1 = [int(x) for x in l1][::-1]
        l2 = [int(x) for x in l2][::-1]
        l1 = int(''.join(str(l) for l in l1))
        l2 = int(''.join(str(l) for l in l2))
        return build_linked_list([int(n) for n in str(l1 + l2)][::-1])
```

---

### ⚠️ Problem with This Method

- Too many conversions and reversals
- More memory usage
- Not the most efficient

---

## ⚙️ Second Idea – Go Digit by Digit

This method does the addition **digit by digit**, just like elementary school math!

---

### 🧩 Optimized Solution

It handles carry-over properly and builds the linked list on the go.

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        ret = r
        Sum = 0
        while l1 or l2:
            if l1:
                Sum += l1.val
                l1 = l1.next
            if l2:
                Sum += l2.val
                l2 = l2.next
            ret.next = ListNode(Sum % 10)
            ret = ret.next
            Sum = Sum // 10
        if Sum > 0:
            ret.next = ListNode(Sum)
        return r.next
```

---

### ✅ Why This Is Better

- No need to convert to/from integers
- Works for very large numbers
- More efficient and clean

---

## 🔗 My Code on GitHub

You can check out the full code here:  
[👉 add-two-numbers.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/2-add-two-numbers.py)
