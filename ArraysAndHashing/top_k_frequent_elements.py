class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums: d[n] = d.get(n, 0) + 1

        d_sorted = sorted(d.items(), key=lambda item: item[1])

        r = [] # result
        for i in range(k):
            (x,y) = d_sorted.pop()

            r.append(x)

        return r