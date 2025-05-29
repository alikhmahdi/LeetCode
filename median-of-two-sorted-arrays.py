num1 = [float(x) for x in input().strip("[]").split(',')]
num2 = [float(x) for x in input().strip("[]").split(',')]
nums = (num1+num2)
nums.sort()
if len(nums) % 2 != 0:
    print(nums[(len(nums)//2)])
else:
    print((nums[len(nums)//2]+nums[(len(nums)//2)-1])/2)
##################################################################


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = (nums1+nums2)
        nums.sort()
        if len(nums) % 2 != 0:
            return (float(nums[(len(nums)//2)]))
        else:
            return (float((nums[len(nums)//2]+nums[(len(nums)//2)-1])/2))
