# Well, Well...

I tried solving the problem [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/) using **Python 3**. That’s when I encountered `ListNode`. I had to figure out what it actually is.

---

## 🚀 Let's Start

### 🤔 Intuition

A **linked list** is a data structure made up of **nodes**, where each node contains a value and a reference (or pointer) to the **next node** in the sequence.

Think of it like a **chain** made of rings — each ring is connected to the next. A linked list works similarly: each node has its own value and a pointer to the next one in line.

---

## 🛠️ How It Works

### ➔ Defining a singly linked list node:

```python
class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None
```

* `val` holds the value of the node.
* `next` points to the next node in the list.

---

### ➔ Creating the list:

```python
for n in range(5, -1, -1):
    if n == 5:
        header = ListNode(n)
        nums = header
    else:
        nums.next = ListNode(n)
        nums = nums.next
```

* For `n == 5`: we create the **head node** (`header`) and start building from there.
* For other values: we link each new node to the previous one using `.next`.

This is how we build the chain.

---

### ➔ Traversing and printing the list:

```python
while header.next or header.val is not None:
    print(header.val)
    if header.next:
        header = header.next
    else:
        break
```

* We use `while header.next or header.val is not None` to ensure the **last node** gets printed.
* The loop continues until we reach the end of the list (`next == None`).

---

## 📌 Linked List Diagram

Here’s a simple visual to understand how a linked list looks:

```
[5] → [4] → [3] → [2] → [1] → [0] → None
```

---

## 🔗 My Code on GitHub

You can check out the full code here:
[👉 linked-list.py on GitHub](https://github.com/alikhmahdi/LeetCode/blob/main/2-linked-list.py)
