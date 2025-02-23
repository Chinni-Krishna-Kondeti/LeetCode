import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        index = -1
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                if index == -1:
                    index = i
                else:
                    return [0] * n
        if index == -1:
            for i in range(n):
                nums[i] = prod // nums[i]
            return nums
        else:
            output = [0]*n
            output[index] = prod
            return output