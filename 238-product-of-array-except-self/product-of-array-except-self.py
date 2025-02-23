import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in nums:
            if i != 0:
                prod *= i
        count = nums.count(0)
        if count == 0:
            for i in range(len(nums)):
                nums[i] = prod // nums[i]
        elif count == 1:
            for i in range(len(nums)):
                nums[i] = prod if nums[i] == 0 else 0
        else:
            nums = [0] * len(nums)
        return nums