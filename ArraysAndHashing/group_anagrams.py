class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            d[sorted_s] = d.get(sorted_s, []) + [s]

        return d.values()