class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsFrequency = {}

        for n in nums:
            numsFrequency[n] = 1 + numsFrequency.get(n, 0)
            
            if numsFrequency[n] > 1:
                return True
        
        return False 
        