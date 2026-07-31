class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = rob2
            rob2 = max(nums[i] + rob1, rob2)
            rob1 = temp

        return rob2