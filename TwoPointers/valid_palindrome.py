class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowers = s.lower()

        alphanum_str = ''

        for c in lowers:
            if c.isalnum():
                alphanum_str += c
        
        return alphanum_str == alphanum_str[::-1]