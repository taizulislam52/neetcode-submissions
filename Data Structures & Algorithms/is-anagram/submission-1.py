class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charFrequency = {}

        for c in s:
            charFrequency[c] = 1 + charFrequency.get(c, 0)
        
        for c in t:
            if c not in charFrequency:
                return False
            charFrequency[c] = 1 + charFrequency.get(c, 0)
        
        for count in charFrequency.values():
            if count % 2 != 0:
                return False
        
        return True
        