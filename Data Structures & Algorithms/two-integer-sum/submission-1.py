class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndices = {}

        for i, n in enumerate(nums):
            if target - n in mapIndices:
                index = mapIndices[target - n]
                return [index, i]
            
            mapIndices[n] = i
        
        return []