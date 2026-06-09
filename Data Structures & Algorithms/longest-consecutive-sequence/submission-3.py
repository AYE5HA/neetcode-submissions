class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        c=0
        for i in m:
            if (i-1) not in m:
                l = 1
                while (i+l) in m:
                    l+=1
                c = max(c, l)  
        return c