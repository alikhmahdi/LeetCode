# x = str(int(input()))
# r = True
# for i in range(len(x)//2):
#     if x[i] != x[-i-1]:
#         r = False
#         break
# print(r)
# #################################################################


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = str(x)
#         r = True
#         for i in range(len(x)//2):
#             if x[i] != x[-i-1]:
#                 r = False
#                 break
#         return r
#################################################################


x = list(str(input()))
print(x[::]==x[::-1])
#################################################################


