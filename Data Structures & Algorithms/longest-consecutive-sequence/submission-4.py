class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        

        nums = list(set(nums))
        nums.sort()
        longest_sequence = {1}

        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count +=1
            else:
                count = 1
            
            longest_sequence.add(count)
        
        return max(longest_sequence)
        