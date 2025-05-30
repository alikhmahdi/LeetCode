class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


for n in range(5, -1, -1):
    if n == 5:
        header = ListNode(n)
        nums = header
    else:
        nums.next = ListNode(n)
        nums = nums.next
while header.next or header.val != None:
    print(header.val)
    if header.next:
        header = header.next
    else:
        break
