class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)

        for i in range(len(nums)):
            if i not in seen:
                return i
                
        return len(nums)