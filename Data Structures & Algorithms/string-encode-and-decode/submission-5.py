class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'e0pty'
        
        return "taijul".join(strs)


    def decode(self, s: str) -> List[str]:
        if s == 'e0pty':
            return []

        return s.split("taijul")
