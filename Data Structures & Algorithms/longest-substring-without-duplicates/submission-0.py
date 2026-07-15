class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        for i in range(len(s)):
            sub = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in sub:
                    sub += s[j]
                else:
                    break
            
            longest = max(longest, len(sub))

        return longest


        