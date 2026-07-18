class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        left = 0
        right = len(numbers) - 1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
        
            if tmp == target:
                res.append(left + 1)
                res.append(right + 1)
                break

        return res