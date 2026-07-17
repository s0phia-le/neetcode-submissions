class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        if len(nums) == 0:
            return 0
        nums.sort()
        curr = nums[0]
        streak = 0
        
        i = 0
        while i < len(nums):
            if curr != nums[i]: # curr is 1 greater than previous number
                curr = nums[i]
                streak = 0

            while i < len(nums) and nums[i] == curr: # looks for numbers that match curr
                i += 1

            streak += 1
            curr += 1 # update curr to next consecutive integer
            res = max(res, streak)

        return res