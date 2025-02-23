class Solution:
    def hIndex(self, citations: List[int]) -> int:
        output = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                output = i + 1
            else:
                break
        return output