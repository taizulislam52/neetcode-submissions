class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_index = 0
        last_numner = 0
        for i in range(len(numbers)):
            n = target - numbers[i]
            if n in numbers[i+1:]:
                first_index = i
                last_numner = n
                break
        
        for i in range(first_index+1, len(numbers)):
            if last_numner == numbers[i]:
                return [first_index+1, i+1]


        