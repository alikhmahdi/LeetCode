s = input()
r = 0
for i in range(len(s)):
    l = []
    realize = 0
    for i1 in range(i, len(s)):
        if not (s[i1] in l):
            realize += 1
            l.append(s[i1])
        else:
            break
    if r < realize:
        r = realize
print(r)
#################################################################


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            l = []
            realize = 0
            for i1 in range(i, len(s)):
                if not (s[i1] in l):
                    realize += 1
                    l.append(s[i1])
                else:
                    break
            if r < realize:
                r = realize
        return r
