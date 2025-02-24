import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        prd = 1
        for i in range(n-2, -1, -1):
            prd *= nums[i+1]
            output[i] *= prd
        return output