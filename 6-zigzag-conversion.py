s = input()
numRows = int(input())
r = ['' for i in range(numRows)]
for i in range(len(s)):
    if numRows > 1:
        n = i % ((numRows*2)-2)
    else:
        n = i % (1)
    if n < numRows:
        r[n] += s[i]
    else:
        r[-(n-numRows)-2] += s[i]
print(''.join(r))
print(r)
#################################################################


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = ['' for i in range(numRows)]
        for i in range(len(s)):
            if numRows > 1:
                n = i % ((numRows*2)-2)
            else:
                n = i % (1)
            if n < numRows:
                r[n] += s[i]
            else:
                r[-(n-numRows)-2] += s[i]
        return ''.join(r)
