class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for i in nums:
            if sub[-1] < i:
                sub.append(i)
            else:
                idx = bisect_left(sub, i)
                sub[idx] = i
        return len(sub)