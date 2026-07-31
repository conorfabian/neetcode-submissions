class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = rob2
            rob2 = max(nums[i] + rob1, rob2)
            rob1 = temp

        return rob2