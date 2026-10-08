class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        dp[-1] = True
        for curr_idx in range(len(nums) - 2, -1, -1):
            val = nums[curr_idx]
            for offset in range(1, val + 1):
                if dp[curr_idx + offset]:
                    dp[curr_idx] = True
                    break

        print(dp)
        return dp[0]