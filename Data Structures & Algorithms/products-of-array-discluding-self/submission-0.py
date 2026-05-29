class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        r = 1
        for i in range(len(nums)):
            res[i] = r
            r *= nums[i]
        l = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= l
            l *= nums[i]
        return res