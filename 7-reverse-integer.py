x = int(input())
if x >= 0:
    r = int(''.join([n for n in str(x)][::-1]))
else:
    x = -x
    r = int(''.join([n for n in str(x)][::-1]))
    r = -r
if -2**31-1 < r < 2**31-1:
    print(r)
else:
    print(0)
#################################################################


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            r = int(''.join([n for n in str(x)][::-1]))
        else:
            x = -x
            r = int(''.join([n for n in str(x)][::-1]))
            r = -r
        if -2**31-1 < r < 2**31-1:
            return r
        else:
            return 0
