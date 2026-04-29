class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, c in enumerate(nums):
            x = target - nums[i]
            if x in mp:
                return [mp[x], i]
            mp[c] = i