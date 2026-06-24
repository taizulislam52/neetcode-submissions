class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
       
        init = ord('a')
        weight = [0] * 26

        for i in range(len(s)):
            if s[i] not in t or t[i] not in s:
                return False
            weight[ord(s[i]) - init] += 1
            weight[ord(t[i]) - init] -= 1
        
        for count in weight:
            if count != 0:
                return False
        
        return True 
        