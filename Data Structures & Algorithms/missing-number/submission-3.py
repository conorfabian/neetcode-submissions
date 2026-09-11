class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)

        for i, num in enumerate(nums):
            total ^= i
            total ^= num

        return total