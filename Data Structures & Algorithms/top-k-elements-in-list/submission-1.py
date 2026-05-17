import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0)+1
        bucket = [[] for i in range(len(nums)+1)]
        for i, x in mp.items():
            bucket[x].append(i)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for x in bucket[i]:
                res.append(x)
                if len(res)==k:
                    return res