l1 = input()
l1 = l1.strip("[]")
l1 = [int(x) for x in l1.split(',')][::-1]
l2 = input()
l2 = l2.strip("[]")
l2 = [int(x) for x in l2.split(',')][::-1]
l1 = int(''.join(str(l) for l in l1))
l2 = int(''.join(str(l) for l in l2))
print([int(n) for n in str(l1+l2)][::-1])
##################################################################


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = linked_list_to_list(l1)
        l2 = linked_list_to_list(l2)
        l1 = [int(x) for x in l1][::-1]
        l2 = [int(x) for x in l2][::-1]
        l1 = int(''.join(str(l) for l in l1))
        l2 = int(''.join(str(l) for l in l2))
        return build_linked_list([int(n) for n in str(l1+l2)][::-1])
#################################################################


l1 = input()
l1 = l1.strip("[]")
l1 = [int(x) for x in l1.split(',')][::-1]
l2 = input()
l2 = l2.strip("[]")
l2 = [int(x) for x in l2.split(',')][::-1]
ret = []
Sum = 0
s = 0
while True:
    if s < len(l1):
        Sum += l1[s]
    if s < len(l2):
        Sum += l2[s]
    if s >= len(l1) and s >= len(l2):
        break
    ret.append(Sum % 10)
    Sum = Sum//10
    s += 1
print(ret)
#################################################################


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
            Sum = Sum//10
        if Sum > 0:
            ret.next = ListNode(Sum % 10)
            ret = ret.next
        return r.next
