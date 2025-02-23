class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_pos = 0
        step_count = 0
        max_reach = 0
        curr_max_reach_pos = 0
        while max_reach < len(nums) - 1:
            curr_reach =  curr_pos + nums[curr_pos]
            if curr_max_reach_pos < curr_pos:
                curr_max_reach_pos = max_reach
                step_count += 1
            if curr_reach >= len(nums) - 1:
                step_count += 1
                break
            if curr_reach > max_reach:
                max_reach = curr_reach
            curr_pos += 1
        return step_count