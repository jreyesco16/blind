class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for n in nums: d[n] = d.get(n, 0) + 1

        x = sorted(d.items(), key=lambda item: item[1])
        
        l = []

        for i in range(k):
            (j, c) = x.pop()
            l.append(j)
        

        return l