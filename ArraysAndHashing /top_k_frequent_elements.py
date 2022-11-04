class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0) + 1

        sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))

        return list(sorted_d.keys())[:k]