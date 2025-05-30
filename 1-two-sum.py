nums = input()
nums = nums.strip("[]")
nums = [int(x) for x in nums.split(',')]
target = int(input())
for index1 in range(len(nums)):
    for index2 in range(index1+1, len(nums)):
        if target == nums[index1]+nums[index2]:
            print([index1, index2])



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            for index2 in range(index1+1, len(nums)):
                if target == nums[index1]+nums[index2]:
                    return ([index1, index2])
                
                

##################################################################
nums = input()
nums = nums.strip("[]")
nums = [int(x) for x in nums.split(',')]
target = int(input())
for num1 in nums:
    for num2 in nums[nums.index(num1)+1::]:
        if target == num1+num2:
            print([nums.index(num1), nums.index(num2)])



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1 in nums:
            for num2 in nums[nums.index(num1)+1::]:
                if target == num1+num2:
                    return [nums.index(num1), nums.index(num2)]
