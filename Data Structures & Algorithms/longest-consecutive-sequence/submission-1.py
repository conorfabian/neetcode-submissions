class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        res = 0
        for num in nums:
            if num - 1 in seen:
                continue

            length = 0
            while num + length in seen:
                length += 1
            res = max(res, length)

        return res