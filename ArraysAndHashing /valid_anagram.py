class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sD, tD = {}, {}
        
        for i in range(len(s)):
            sD[s[i]], tD[t[i]] = 1 + sD.get(s[i], 0), 1 + tD.get(t[i], 0)
        
        for k in sD:
            if sD[k] != tD.get(k, 0):
                return False
        
        return True