class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_pal = ""

        for i in range(0, len(s)):
            if len(longest_pal) > len(s)-i:
                    return longest_pal

            for j in reversed(range(i, len(s)+1)):
                sub_str = s[i:j]

                if self.isPanlindrome(sub_str):
                    longest_pal = max([longest_pal, sub_str], key=len)
            
        return longest_pal

    def isPanlindrome(self, s:str) -> bool:
        return s == s[::-1]
        