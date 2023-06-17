class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            res = ''.join(sorted(s))

            d[res] = d.get(res, []) + [s] 

        return d.values()