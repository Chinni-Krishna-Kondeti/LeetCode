class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        n = 1
        while i>=0:
            if i == 0:
                return nums[0] >= n
            if nums[i] >= n:
                n = 1
            else:
                n += 1
            i -= 1
        return True