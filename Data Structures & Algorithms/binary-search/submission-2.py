class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        low = 0
        hi = len(nums) - 1

        while low <= hi:
            mid = low + (hi - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
                
        return -1