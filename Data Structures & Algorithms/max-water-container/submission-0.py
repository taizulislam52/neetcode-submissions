class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContainer = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                 maxContainer = max(maxContainer, min(heights[i], heights[j]) * (j - i))
            
        
        return maxContainer

        