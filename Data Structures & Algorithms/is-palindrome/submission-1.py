class Solution:
    def isAlNum(self, c):
        code = ord(c)
        return 48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122
        
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        
        
        while front < back:
            while front < back and not self.isAlNum(s[front]):
                front +=1
            
            while back > front and not self.isAlNum(s[back]):
                back -=1

            if s[back].lower() != s[front].lower():
                return False
            
            back -=1
            front +=1
            
        return True
        