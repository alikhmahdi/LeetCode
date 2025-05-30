s = input()
chars = ''
for i1 in range(len(s)):
    for i2 in range(i1, len(s)+1):
        if s[i1:i2+1] == s[i1:i2+1][::-1] and i2-i1+1 > len(chars):
            chars = s[i1:i2+1]
print(chars)
##################################################################


class Solution:
    def longestPalindrome(self, s: str) -> str:
        chars = ''
        for i1 in range(len(s)):
            for i2 in range(i1, len(s)+1):
                if s[i1:i2+1] == s[i1:i2+1][::-1] and i2-i1+1 > len(chars):
                    chars = s[i1:i2+1]
        return chars
