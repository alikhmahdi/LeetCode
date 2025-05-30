s = input()
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
        r = r*10+int(c)
        end = True
if negtive and r < 2**31:
    print(-r)
if negtive:
    print(-2**31)
elif r < 2**31:
    print(r)
else:
    print((2**31)-1)
#################################################################


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
                r = r*10+int(c)
                end = True
        if negtive and r < 2**31:
            return -r
        elif negtive:
            return -2**31
        elif r < 2**31:
            return r
        else:
            return (2**31)-1
