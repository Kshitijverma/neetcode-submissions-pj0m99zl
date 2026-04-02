class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for n in nums:
            occ = nums.count(n)
            x = 1
            while x < occ:
                nums.remove(n)
                x=x+1

        return len(nums)