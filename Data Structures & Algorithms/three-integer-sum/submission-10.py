class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            target = -nums[i]

            while j < k:
                curr = nums[j] + nums[k]

                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    tmp = [nums[i], nums[j], nums[k]]
                    if tmp not in res:
                        res.append(tmp)
                    j += 1
                    k -= 1
                        
                    continue
        return res