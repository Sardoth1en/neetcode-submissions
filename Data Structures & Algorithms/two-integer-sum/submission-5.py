class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for i , n in enumerate(nums):
            wanted = target - n
            if wanted in hasmap:
                return [hasmap[wanted], i]
            hasmap[n] = i
                