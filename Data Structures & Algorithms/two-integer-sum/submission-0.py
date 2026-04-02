class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder not in map:
                map[nums[i]] = i
            else:
                return [map[remainder], i]