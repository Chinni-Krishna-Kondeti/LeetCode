class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        data = dict()
        output = []
        for i in range(len(numbers)):
            res = target - numbers[i]
            if res not in data:
                data[numbers[i]] = i
            else:
                output = [data[res]+1, i+1]
                break
        return output