class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        b = j
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                a = height[i] * b
                i += 1
            else:
                a = height[j] * b
                j -= 1
            max_area = max(max_area, a)
            b -= 1
        return max_area