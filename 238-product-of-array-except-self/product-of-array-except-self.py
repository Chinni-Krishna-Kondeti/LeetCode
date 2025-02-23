class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        n = len(nums)
        count = nums.count(0)
        if count > 1:
            return [0] * n
        index = -1
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                index = i
        if count == 1:
            output = [0] * n
            output[index] = prod
            return output
        for i in range(n):
            nums[i] = prod // nums[i]
        return nums