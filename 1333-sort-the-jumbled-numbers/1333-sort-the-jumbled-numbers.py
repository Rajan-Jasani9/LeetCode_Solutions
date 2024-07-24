class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            x = ''.join(list(map(lambda x: str(mapping[int(x)]), str(nums[i]) )))
            nums[i] = (int(x),int(nums[i]))

        nums = sorted(nums, key=lambda x: x[0])

        return [x[1] for x in nums]