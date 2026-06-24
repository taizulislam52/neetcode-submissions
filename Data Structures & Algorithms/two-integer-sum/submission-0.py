class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndices = {}

        for i, n in enumerate(nums):
            if target - n in mapIndices:
                index = mapIndices[target - n]
                return [index, i]
            else:
                mapIndices[n] = i
        
        return []