class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = sum(nums)
        n = len(nums)
        res = []
        sum_till = 0
        for i in range(n):
            prefix -= nums[i]
            res.append(   abs(nums[i]*(i) - sum_till)  +  abs(prefix - (nums[i]*(n-i-1))) )
            sum_till += nums[i]

        return res
        